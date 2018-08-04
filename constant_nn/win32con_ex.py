


#for import win32con_ex as win32con
from win32con import *

MAPVK_VK_TO_VSC = 0
WM_MOUSEHWHEEL = 0x020E
MOUSEEVENTF_HWHEEL = 0x01000


#WM_MOUSEWHEEL = 0x020A
'''
WM_MOUSEWHEEL message

Parameters

wParam
The high-order word indicates the distance the wheel is rotated, expressed in multiples or divisions of WHEEL_DELTA, which is 120. A positive value indicates that the wheel was rotated forward, away from the user; a negative value indicates that the wheel was rotated backward, toward the user.
The low-order word indicates whether various virtual keys are down. This parameter can be one or more of the following values.
Value	Meaning
MK_CONTROL
0x0008
The CTRL key is down.
MK_LBUTTON
0x0001
The left mouse button is down.
MK_MBUTTON
0x0010
The middle mouse button is down.
MK_RBUTTON
0x0002
The right mouse button is down.
MK_SHIFT
0x0004
The SHIFT key is down.
MK_XBUTTON1
0x0020
The first X button is down.
MK_XBUTTON2
0x0040
The second X button is down.
 
lParam
The low-order word specifies the x-coordinate of the pointer, relative to the upper-left corner of the screen.
The high-order word specifies the y-coordinate of the pointer, relative to the upper-left corner of the screen.
Return value

If an application processes this message, it should return zero.
Remarks

Use the following code to get the information in the wParam parameter:

fwKeys = GET_KEYSTATE_WPARAM(wParam);
zDelta = GET_WHEEL_DELTA_WPARAM(wParam);

Use the following code to obtain the horizontal and vertical position:

xPos = GET_X_LPARAM(lParam); 
yPos = GET_Y_LPARAM(lParam); 

As noted above, the x-coordinate is in the low-order short of the return value; the y-coordinate is in the high-order short (both represent signed values because they can take negative values on systems with multiple monitors). If the return value is assigned to a variable, you can use the MAKEPOINTS macro to obtain a POINTS structure from the return value. You can also use the GET_X_LPARAM or GET_Y_LPARAM macro to extract the x- or y-coordinate.
Important  Do not use the LOWORD or HIWORD macros to extract the x- and y- coordinates of the cursor position because these macros return incorrect results on systems with multiple monitors. Systems with multiple monitors can have negative x- and y- coordinates, and LOWORD and HIWORD treat the coordinates as unsigned quantities.
The wheel rotation will be a multiple of WHEEL_DELTA, which is set at 120. This is the threshold for action to be taken, and one such action (for example, scrolling one increment) should occur for each delta.
The delta was set to 120 to allow Microsoft or other vendors to build finer-resolution wheels (a freely-rotating wheel with no notches) to send more messages per rotation, but with a smaller value in each message. To use this feature, you can either add the incoming delta values until WHEEL_DELTA is reached (so for a delta-rotation you get the same response), or scroll partial lines in response to the more frequent messages. You can also choose your scroll granularity and accumulate deltas until it is reached.
Note, there is no fwKeys for MSH_MOUSEWHEEL. Otherwise, the parameters are exactly the same as for WM_MOUSEWHEEL.
It is up to the application to forward MSH_MOUSEWHEEL to any embedded objects or controls. The application is required to send the message to an active embedded OLE application. It is optional that the application sends it to a wheel-enabled control with focus. If the application does send the message to a control, it can check the return value to see if the message was processed. Controls are required to return a value of TRUE if they process the message.
'''
