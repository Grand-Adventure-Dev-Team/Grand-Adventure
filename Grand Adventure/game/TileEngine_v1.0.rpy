# TILE ENGINE
# Contents:
#  Ren'Py style definitions
#  Struct object definition
#  TileEngine class definition
#  Sprite class definition
#  Utility function definitions

init -10 python:
  import copy

  ##########################
  ### Ren'Py definitions ###
  ##########################
  # Put the 'tileengine' layer in config.layers.
  # This could be vulnerable if the user sets config.layers in their own code.
  if 'tileengine' not in config.layers:
    config.layers = [ 'master', 'tileengine', 'transient', 'overlay' ]

  # Define Ren'Py styles used by the UnitEngine:
  style.engine_frame = Style(style.frame)
  style.engine_button = Style(style.button)
  style.engine_button_text = Style(style.button_text)
  style.engine_label = Style(style.label)
  style.engine_label_text = Style(style.label_text)
  style.engine_scrollbar = Style(style.scrollbar)
  style.engine_vscrollbar = Style(style.vscrollbar)
  style.engine_menu = Style(style.menu)
  style.engine_frame["done button"].xalign  = 0.5

  # General functions to draw buttons and text
  def engine_button(text, **kwargs):
    ui.textbutton(
        _(text),
        style=style.engine_button[text],
        text_style=style.engine_button_text[text],
        **kwargs)
  def engine_label(text, **kwargs):
    ui.window(style=style.engine_label[text], **kwargs)
    ui.text(_(text), style=style.engine_label_text[text], **kwargs)

  ###################################
  ### Definition of Struct object ###
  ###################################
  class Struct(object):
    """Simple object to store arbitrary parameters.

    Any Python object will let you self obj.newfield = val
    unless it's explicitly prohibited; Structs just make it
    one step easier by allowing
      obj = Struct(field1 = val1, field2 = val2)
    The TileEngine, UnitEngine, and Unit objects are all
    derived from Struct, to make defining new parameters
    as easy as possible.
    """

    def __init__(self, **data):
      """The __init__ function is the one that does all the work."""
      if data:
        vars(self).update(data)
    def __setstate__(self, data):
      vars(self).update(data)
    def __getstate__(self):
      return vars(self)

  #######################################
  ### Definition of TileEngine object ###
  #######################################
  class TileEngine(Struct):
    """Engine to display a tile-based map, and sprites on it.

    Required parameters:
    map:
      The 2-dimensional array of tiles. Each tile must be an object (for
      example, a Struct) with properties lower and upper, each of which can
      be None, or the name of a Ren'Py Image defined with the Image statement.
    tilewidth, tileheight:
      The full width and height of one tile, in pixels.
    screenwidth, screenheight:
      The desired width and height of the viewport, in pixels.

    Optional parameters:
    geometry = TileEngine.ISOMETRIC:
      Whether the map should be displayed in an isometric view or as a straight
      grid. This should be either TileEngine.ISOMETRIC or TileEngine.STRAIGHT.
    cursor_sprite = "cursor":
      name of a Ren'Py Image to use as the cursor.
    show_cursor = False:
      Whether or not to show a cursor.
      Note that False leaves mouseless players unable to move.
    background = None:
      If not None, when the TileEngine is created, the scene will be cleared
      and this image displayed with renpy.show().
    layer = "tileengine":
      Which layer to display the map on.
    movement_duration = 0.5:
      When Sprites are moved from one map square to another, how long those
      moves should take.

    All of the above parameters are made available as properties of the
    TileEngine object. The following additional properties are provided:
    gxmax, gymax:
      Size of the map in tiles.
    cursor:
      A Sprite object representing the cursor, if show_cursor is True.
    sprites:
      List of the Sprite objects attached to the TileEngine. If show_cursor
      is true, then the cursor will be in this list.
    """

    # Constants that're available before instantiation:
    # The Directions constants
    ISO_DIR_W       = Struct(dx = -1, dy = -1, name = "w")
    ISO_DIR_SW      = Struct(dx = 0,  dy = -1, name = "sw")
    ISO_DIR_S       = Struct(dx = +1, dy = -1, name = "s")
    ISO_DIR_NW      = Struct(dx = -1, dy = 0,  name = "nw")
    ISO_DIR_NEUTRAL = Struct(dx = 0,  dy = 0,  name = "")
    ISO_DIR_SE      = Struct(dx = +1, dy = 0,  name = "se")
    ISO_DIR_N       = Struct(dx = -1, dy = +1, name = "n")
    ISO_DIR_NE      = Struct(dx = 0,  dy = +1, name = "ne")
    ISO_DIR_E       = Struct(dx = +1, dy = +1, name = "e")
    STRAIGHT_DIR_NW      = Struct(dx = -1, dy = -1, name = "nw")
    STRAIGHT_DIR_N       = Struct(dx = 0,  dy = -1, name = "n")
    STRAIGHT_DIR_NE      = Struct(dx = +1, dy = -1, name = "ne")
    STRAIGHT_DIR_W       = Struct(dx = -1, dy = 0,  name = "w")
    STRAIGHT_DIR_NEUTRAL = Struct(dx = 0,  dy = 0,  name = "")
    STRAIGHT_DIR_E       = Struct(dx = +1, dy = 0,  name = "e")
    STRAIGHT_DIR_SW      = Struct(dx = -1, dy = +1, name = "sw")
    STRAIGHT_DIR_S       = Struct(dx = 0,  dy = +1, name = "s")
    STRAIGHT_DIR_SE      = Struct(dx = +1, dy = +1, name = "se")
    # The Directions arrays are in order of ascending dy then dx:
    # This is required by the Direction() function.
    ISO_Directions = [ISO_DIR_W, ISO_DIR_SW, ISO_DIR_S, ISO_DIR_NW, ISO_DIR_NEUTRAL, ISO_DIR_SE, ISO_DIR_N, ISO_DIR_NE, ISO_DIR_E]
    STRAIGHT_Directions = [STRAIGHT_DIR_NW, STRAIGHT_DIR_N, STRAIGHT_DIR_NE, STRAIGHT_DIR_W, STRAIGHT_DIR_NEUTRAL, STRAIGHT_DIR_E, STRAIGHT_DIR_SW, STRAIGHT_DIR_S, STRAIGHT_DIR_SE]

    # Geometry constants
    ISOMETRIC = 1
    STRAIGHT = 2

    def __init__(self, map, tilewidth, tileheight,
      screenwidth = config.screen_width, screenheight = config.screen_height,
      cursor_sprite = "cursor", show_cursor = False, draggable=False,
      background = None, geometry = ISOMETRIC,
      layer = 'tileengine', movement_duration = 0.5,
      xmargin = 100, ymargin = 100,
      keymap = None,
      **properties):

      # Assign default values to non-input properties
      self.Sprites = [ ]
      self.Cursor = None
      self.DebugString = ""

      # Assign properties passed directly as inputs
      self.geometry = geometry
      self.map = map
      self.tilewidth = tilewidth
      self.tileheight = tileheight
      self.screenwidth = screenwidth
      self.screenheight = screenheight
      self.xmargin = xmargin
      self.ymargin = ymargin
      self.cursor_sprite = cursor_sprite
      self.movement_duration = movement_duration
      self.draggable = draggable
      # show_cursor is assigned later
      self.layer = layer

      # Default background
      if background is not None:
        renpy.scene()
        renpy.show(background)
      self.background = background

      # Assign properties derived from inputs
      self.gxmax = len(map)
      self.gymax = len(map[0])

      if self.geometry == self.ISOMETRIC:
        self.divisor = 2
        self.tileswidth = self.gxmax + self.gymax
        self.tilesheight = self.gxmax + self.gymax
        self.SXOffset = -self.xmargin
        self.SYOffset = -self.ymargin - (self.tileheight * self.gymax / self.divisor)
        self.GridRelToScreen = self.GridRelToScreenIsometric
        self.ScreenToGridRel = self.ScreenToGridRelIsometric
        self.Directions = self.ISO_Directions
        (self.DIR_W, self.DIR_SW, self.DIR_S, self.DIR_NW, self.DIR_NEUTRAL, self.DIR_SE, self.DIR_N, self.DIR_NE, self.DIR_E) = (self.ISO_DIR_W, self.ISO_DIR_SW, self.ISO_DIR_S, self.ISO_DIR_NW, self.ISO_DIR_NEUTRAL, self.ISO_DIR_SE, self.ISO_DIR_N, self.ISO_DIR_NE, self.ISO_DIR_E)

        # For isometric grids, the conversion function from a
        # screen count (sxt, syt) to an actual screen coordinate (sx, sy)
        # is a multiplication by tilewidth/2 or tileheight/2,
        # plus a half-width step every other row,
        # offset by self.SXOffset and self.SYOffset
        self.ScreenCountConversionFunc = lambda (sxt, syt): (
            sxt*self.tilewidth + (syt % 2) * self.tilewidth + self.xmargin,
            syt*self.tileheight/2 + self.ymargin)
        if keymap is None:
          keymap = {
            'K_LEFT':  ui.returns(self.MoveCursor(self, self.DIR_NW)),
            'K_RIGHT': ui.returns(self.MoveCursor(self, self.DIR_SE)),
            'K_UP':    ui.returns(self.MoveCursor(self, self.DIR_NE)),
            'K_DOWN':  ui.returns(self.MoveCursor(self, self.DIR_SW)),
            'K_KP4':   ui.returns(self.MoveCursor(self, self.DIR_NW)),
            'K_KP6':   ui.returns(self.MoveCursor(self, self.DIR_SE)),
            'K_KP8':   ui.returns(self.MoveCursor(self, self.DIR_NE)),
            'K_KP2':   ui.returns(self.MoveCursor(self, self.DIR_SW)),
              }

      else:
        self.divisor = 1
        self.tileswidth = self.gxmax
        self.tilesheight = self.gymax
        self.SXOffset = -self.xmargin
        self.SYOffset = -self.ymargin
        self.GridRelToScreen = self.GridRelToScreenStraight
        self.ScreenToGridRel = self.ScreenToGridRelStraight
        self.Directions = self.STRAIGHT_Directions
        (self.DIR_W, self.DIR_SW, self.DIR_S, self.DIR_NW, self.DIR_NEUTRAL, self.DIR_SE, self.DIR_N, self.DIR_NE, self.DIR_E) = (self.STRAIGHT_DIR_W, self.STRAIGHT_DIR_SW, self.STRAIGHT_DIR_S, self.STRAIGHT_DIR_NW, self.STRAIGHT_DIR_NEUTRAL, self.STRAIGHT_DIR_SE, self.STRAIGHT_DIR_N, self.STRAIGHT_DIR_NE, self.STRAIGHT_DIR_E)
        # For straight grids, the conversion function from a
        # screen count (sxt, syt) to an actual screen coordinate (sx, sy)
        # is a simple multiplication by tilewidth or tileheight,
        # offset by self.SXOffset and self.SYOffset
        self.ScreenCountConversionFunc = lambda (sxt, syt): (
            sxt*self.tilewidth + self.xmargin,
            syt*self.tileheight + self.ymargin)
        if keymap is None:
          keymap = {
            'K_LEFT':  ui.returns(self.MoveCursor(self, self.DIR_W)),
            'K_RIGHT': ui.returns(self.MoveCursor(self, self.DIR_E)),
            'K_UP':    ui.returns(self.MoveCursor(self, self.DIR_N)),
            'K_DOWN':  ui.returns(self.MoveCursor(self, self.DIR_S)),
            'K_KP4':   ui.returns(self.MoveCursor(self, self.DIR_W)),
            'K_KP6':   ui.returns(self.MoveCursor(self, self.DIR_E)),
            'K_KP8':   ui.returns(self.MoveCursor(self, self.DIR_N)),
            'K_KP2':   ui.returns(self.MoveCursor(self, self.DIR_S)),
              }

      self.virtual_view_width = self.tilewidth * self.tileswidth / self.divisor + 2 * self.xmargin
      self.virtual_view_height = self.tileheight * self.tilesheight / self.divisor + 2 * self.ymargin

      self.keymap = keymap

      # Define the default callbacks
      self.callbacks = Struct()
      self.callbacks.PreShow = False
      self.callbacks.PostShow = False
      self.callbacks.square_show_pre_sprite = None
      self.callbacks.square_show_post_sprite = None

      # Process unhandled properties
      Struct.__init__(self, **properties)

      # Create the cursor
      if show_cursor:
        self.Cursor = self.Sprite(self.cursor_sprite, (0, 0))
      self.show_cursor = show_cursor

      # Create the viewport adjustments
      self.xadjustment = ui.adjustment(range=self.virtual_view_width)
      self.yadjustment = ui.adjustment(range=self.virtual_view_height)


    # Properties that do special things on setting:
    # When the user sets e.show_cursor to True, create a Cursor sprite.
    # When the user sets e.show_cursor to False, remove the Cursor sprite.
    def Set_show_cursor(self, val):
      self._show_cursor = val
      if val: # Create a cursor
        if not self.Cursor:
          cursorpos = (0, 0)
          self.Cursor = self.Sprite(self.cursor_sprite, cursorpos)
      else: # Hide the cursor
        if self.Cursor:
          self.Cursor.Remove()
          self.Cursor = None
    def Get_show_cursor(self):
      return self._show_cursor
    show_cursor = property(Get_show_cursor, Set_show_cursor)


    ######################## User interface ########################

    # The main Show() function - the heart of the TileEngine.
    def Show(self, interactions=True, **properties):
      """Display the map and sprites.
      The same parameters are supported as TileEngine.Show().
      """
      # Put us on our own layer, and clear it
      ui.layer(self.layer)
      ui.clear()

      # Add the keymap
      ui.keymap(**self.keymap)

      # Start the viewport
      ui.side(['c', 'b', 'r'], spacing=5)
      draggable = self.draggable and interactions
      self.viewport = ui.viewport(draggable=draggable, mousewheel=True, xmaximum=self.screenwidth - 20, ymaximum=self.screenheight - 20, child_size=(self.virtual_view_width, self.virtual_view_height), xalign=0.5, yalign=0.5, xadjustment=self.xadjustment, yadjustment=self.yadjustment)

      # Use a ui.fixed() to group all the tiles and sprites
      # They'll all be positioned with their own ui.add() calls
      ui.fixed()

      # Call the Pre-Show callback
      if self.callbacks.PreShow:
        self.callbacks.PreShow(**properties)


      # Show the tiles and sprites, from top to bottom, so that images lower
      # down the screen are displayed after ones higher up.

      # Count down and across the screen in tile-increments.
      # First, for the lower images (terrain).
      for syt in range(self.tilesheight):
        for sxt in range(self.tileswidth):
          (sx, sy) = self.ScreenCountConversionFunc((sxt, syt))
          (gx, gy) = self.ScreenToGrid((sx, sy))
          (sx, sy) = self.GridToScreen((gx, gy)) # to align properly
          if self.InBounds((gx, gy)):
            if type(self.map[gx][gy].lower) == type(""):
              # If we've been given a string, create an Image() from it
              ui.add(Image(self.map[gx][gy].lower, xpos=sx, ypos=sy, xanchor=0.5, yanchor=1.0))
            elif hasattr(self.map[gx][gy].lower, "function"):
              # If we've been given a general function, call it
              ui.add(self.map[gx][gy].lower.function(xpos=sx, ypos=sy, xanchor=0.5, yanchor=1.0))

      # Count down and across the screen in tile-increments.
      # Now, for the upper images and sprites.
      for syt in range(self.tilesheight):
        for sxt in range(self.tileswidth):
          (sx, sy) = self.ScreenCountConversionFunc((sxt, syt))
          (gx, gy) = self.ScreenToGrid((sx, sy))
          (sx, sy) = self.GridToScreen((gx, gy)) # to align properly
          if self.InBounds((gx, gy)):
            # Call the pre-sprite callback
            if self.callbacks.square_show_pre_sprite:
              self.callbacks.square_show_pre_sprite((gx, gy), (sx, sy))
            # First, show any sprites that're at this position
            for s in [s for s in self.Sprites if s.position==(gx,gy) and s.visible]:
              if s.moving:
                (oldsx, oldsy) = self.GridToScreen(s.OldPos)
                (newsx, newsy) = self.GridToScreen(s.position)
                ui.at(Move((oldsx, oldsy, 0.5, 1.0),
                           (newsx, newsy, 0.5, 1.0),
                           self.movement_duration))
                s.moving = False
                position_params = {}
              else:
                position_params = {"xpos": sx, "ypos": sy, "xanchor": 0.5, "yanchor": 1.0}

              if (interactions) and (s.clicked is not Sprite.DefaultClickedFunction):
                ui.imagebutton(s.function(s.sprite_name),
                               s.function(s.hover_sprite_name),
                               clicked=s.clicked, focus_mask=True, **position_params)
              else:
                ui.add(s.function(s.sprite_name, **position_params))
            # Then, show any obstructions (upper terrain) at this map position
            if type(self.map[gx][gy].upper) == type(""):
              # If we've been given a string, create an Image() from it
              ui.add(Image(self.map[gx][gy].upper, xpos=sx, ypos=sy, xanchor=0.5, yanchor=1.0))
            elif hasattr(self.map[gx][gy].upper, "function"):
              # If we've been given a general function, call it
              ui.add(self.map[gx][gy].upper.function(xpos=sx, ypos=sy, xanchor=0.5, yanchor=1.0))

            # Call the post-sprite callback
            if self.callbacks.square_show_post_sprite:
              self.callbacks.square_show_post_sprite((gx, gy), (sx, sy))


      # Now call the Post-Show callback
      if self.callbacks.PostShow:
        self.callbacks.PostShow(**properties)

      # Close the viewport
      ui.close() # close the ui.fixed() layout
      # Show the scrollbars
      ui.bar(adjustment=self.xadjustment, style=style.engine_scrollbar) # at the bottom, active=interactions
      ui.bar(adjustment=self.yadjustment, style=style.engine_vscrollbar) # at the right, active=interactions
      ui.close() # close the ui.side() layout
      ui.close() # close the ui.layer()

      # Display debug info
      if self.DebugString != "":
        narrator(self.DebugString)
        self.DebugString = ""


    def View(self, show_button=True, xalign=0.5, yalign=0.0, **properties):
      """Let the user view the grid.

      Calls self.Show() once, and then calls ui.interact() in a loop to
      let the user move around using keyboard. The user can press ESCAPE or Q
      to leave the view, or click on the button if show_button is True.

      Parameters:
        show_button = True:
          If True, display a button at the top of the screen that the user can
          click to leave the TileEngine. The button's text will be "Done", although this can be changed using config.translations.
      """
      self.Show()
      retval = False
      while retval is not True:
        ui.keymap(K_ESCAPE=ui.returns(True),
                       K_q=ui.returns(True),
                       **self.keymap)
        if show_button:
          ui.frame(style=style.engine_frame["done button"])
          engine_button("Done", clicked=ui.returns(True))
        retval = ui.interact()
        if callable(retval):
          retval = retval()
      self.Hide()

    def Hide(self):
      """Clear the layer specified in the engine's layer property."""
      ui.layer(self.layer)
      ui.clear()
      ui.close()


    def Sprite(self, sprite_name, position=(None,None), **properties):
      """Create a Sprite object and add it to the tileengine's sprite list.

      Parameters:
        sprite_name:
          Required. Provides the sprite_name for the Sprite, which is a Ren'Py
          Image as defined by the Image statement.
        position = (None, None):
          A 2-element tuple consisting of the Sprite's x and y coordinates
          on the map.
        visible = True:
          If False, this Sprite will not be displayed.
      """
      # create the Sprite object, passing the tile engine as first arg
      spriteObj = Sprite(engine=self, sprite_name=sprite_name,
        position=position, **properties)
      return spriteObj

    # Method MoveCursor(): Curried, so that ui callbacks can curry in the
    # required direction.
    @renpy.curry
    def MoveCursor(self, Direction):
      """Move the cursor in the Direction specified.

      Returns a function which, when called, will move the cursor in the
      specified direction.

      Parameter Direction:
          Must be supplied. Must be a Struct with properties dx and dy.
          Should be one of the TileEngine.DIR_{N,NE,E,SE,S,SW,W,NW} constants.
          The cursor's position will be changed by the values of dx and dy.
      """
      newgx = self.Cursor.position[0] + Direction.dx
      newgy = self.Cursor.position[1] + Direction.dy
      if self.InBounds((newgx,newgy)):
        # CentreViewOn((newgx, newgy)) puts the cursor at (newgx, newgy)
        self.CentreViewOn((newgx, newgy))

    def CentreViewOn(self, (gx, gy)):
      """Centre the viewport on the specified position."""
      if self.Cursor:
        self.Cursor.position = (gx, gy)
      (sx, sy) = self.GridToScreen((gx, gy))
      self.xadjustment.change(sx - self.screenwidth/2)
      self.yadjustment.change(sy - self.screenheight/2)


    ################### CO-ORDINATE CONVERSION FUNCTIONS ###################

    # For isometric view, screen and grid coordinates look like this:
    #    gy            -.
    #   --+    _   +-----+
    #   -'|  _X_   |   -' sx
    # -'   _X_ _  \|/
    #    _X_ _X_   '  sy
    #   <_ _X_ _
    #     X_ _X_
    #       X_ _
    # -.      X_
    #   -.|
    #   --+ gx

    def ScreenToGrid(self, (sx, sy)):
      """Convert the specified screen position to grid co-ordinates."""
      # self.ScreenToGridRel is defined by __init__ as either
      # self.ScreenToGridRelIsometric or self.ScreenToGridRelStraight
      return self.ScreenToGridRel((sx + self.SXOffset, sy + self.SYOffset))

    def ScreenToGridRelIsometric(self, (sx, sy)):
      """Convert the screen position to isometric grid co-ordinates."""
      sxsq = int(sx * 2 / self.tilewidth)
      sysq = int(sy * 2 / self.tileheight)
      gxr = (sxsq + sysq) / 2    # sxsq - sysq
      gyr = (sxsq - sysq) / 2   # -sxsq - sysq
      return (gxr,gyr)

    def ScreenToGridRelStraight(self, (sx, sy)):
      """Convert the screen position to straight grid co-ordinates."""
      gxr = int(sx / self.tilewidth)
      gyr = int(sy / self.tileheight)
      return (gxr,gyr)

    def GridToScreen(self, (gx, gy)):
      """Convert the specified grid position to screen co-ordinates.

      The screen co-ordinates returned will be relative to the top-left
      corner of the viewport, and not necessarily of the actual user's screen.
      """
      (sx, sy) = self.GridRelToScreen((gx, gy))
      return (sx - self.SXOffset, sy - self.SYOffset)

    def GridRelToScreenIsometric(self, (gxr, gyr)):
      """Convert the isometric grid position to screen co-ordinates."""
      sx = ((gxr + gyr) * self.tilewidth) / 2
      sy = ((gxr - gyr) * self.tileheight) / 2
      return (sx, sy)

    def GridRelToScreenStraight(self, (gxr, gyr)):
      """Convert the straight grid position to screen co-ordinates."""
      sx = gxr * self.tilewidth
      sy = gyr * self.tileheight
      return (sx, sy)

    def Direction(self, (dx, dy)):
      """Return a Direction struct corresponding to the specified dx and dy.

      Note that the Directions are different between isometric and straight
      display. For example, e.DIR_NW has (dx,dy) of (+1,-1) in straight
      geometry, but (0,+1) in isometric geometry.
      """
      return self.Directions[dy*3+dx+4]

    def InBounds(self, (gx, gy)):
      """Return True if the specified grid co-ordinates are a valid map square."""
      return (gx>=0 and gx<self.gxmax and gy>=0 and gy<self.gymax)

    def Position(self, (xpos, ypos)):
      """Return a Ren'Py Position object with suitable anchors.

      A Position object is returned, suitable for inclusion in a Ren'Py
      "at" clause or "at_list" parameter. The xanchor is 0.5 and the
      yanchor is 1.0: this allows both isometric and straight tiles to
      have items taller than tileheight display appropriately."""
      return Position(xpos=xpos, ypos=ypos, xanchor=0.5, yanchor=1.0)

  ###################################
  ### Definition of Sprite object ###
  ###################################

  class Sprite(object):
    """A graphical object tied to a particular square of the map.

    Required parameters:
    engine:
      The TileEngine that this Sprite will be attached to.
    sprite_name:
      The name of the Ren'Py Image, as defined by the Image statement, that
      will be displayed on the grid square equal to this sprite's position.

    Optional parameters:
    position = (None, None):
      A 2-element tuple consisting of the Sprite's x and y coordinates
      on the map.
    visible = True:
      If False, this Sprite will not be displayed.
    clicked = None:
      If not None, this must be a function, which will be called when the
      player clicks on the Sprite. This should usually be wrapped in ui.returns().
    hover_sprite_name = sprite_name:
      If clicked is not None, this Image will be displayed when the player
      hovers the mouse over the Sprite.
    """
    # Static properties
    DefaultClickedFunction = ui.returns(None)

    def __init__(self, engine, sprite_name, position=(None, None),
            visible=True,
            function=Image,
            clicked=None,

            hover_sprite_name=None):
      assert engine is not None, "Sprite must be created by a TileEngine's Sprite() function!"
      # Assign properties passed directly as inputs
      self.engine = engine
      self.sprite_name = sprite_name
      self.position = position
      self.visible = visible
      self.function = function

      # Assign properties derived from inputs
      if hover_sprite_name is None:
        hover_sprite_name = sprite_name
      self.hover_sprite_name = hover_sprite_name

      if clicked is None:
        self.clicked = Sprite.DefaultClickedFunction
      else:
        self.clicked = clicked

      # Assign default properties
      self.moving = False

      # Register ourselves with the engine
      self.engine.Sprites.append(self)

    def MoveTo(self, position):
      """Move the Sprite to the new position.

      On the next call to engine.Show(), the Sprite will be displayed as moving
      smoothly to the new grid position, over the course of
      engine.movement_duration seconds.
      """
      self.moving = True
      self.OldPos = self.position
      self.position = position

    def Remove(self):
      """Permanently remove the Sprite from the TileEngine."""
      self.engine.Sprites.remove(self)
      del(self)


  ####################################
  ### Utility function definitions ###
  ####################################
  def sign(n):
    if n>0:
      return 1
    elif n<0:
      return -1
    else:
      return 0