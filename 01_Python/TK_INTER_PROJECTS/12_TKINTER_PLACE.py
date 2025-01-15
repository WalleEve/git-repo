# TKINTER PLACE GEOMETRY MANAGER 
The Tkinter place geometry manager allows us to precisely position widgets within its container using te (x, y) coordinate system
To access the place geometry manager, we use the place() method 
on all the standard widgets like 

widget.place(**options)

Absolute and relative options:
The place geometry manager provides us with both 
absolute and relative positioning options:
. Absolute positioning is specified by the x and y options.
. Relative positions is specified by the relx and rely options.

Specifying width and height 
To set the absolute width and height of the pixels, we use the width and height options.
The place geometry manager also provides us with relative width and height using the relwidth and relheight options.

The relwidth and relheight has a value of a floating-point number between 0.0  and 1.0.
This value represents a fraction of the width and height of the container.

# Anchor:
To specify the exact position of the width, we use the anchor option.
The values of anchor can be N, E, S, W, NW, SE, SW
The anchor defaults to NW which is the pupper let corner of the parent container.

# When to use the Place geometry manager.

In practice, you’ll rarely use the place geometry manager. The reason is that if you make a minor change to the position of a widget, you need to change the position of other widgets, which is very cumbersome.

The place manager is only useful when you want to build applications that allow end-users to decide where to place the widgets on a container.
















