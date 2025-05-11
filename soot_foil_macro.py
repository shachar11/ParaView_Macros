# trace generated using paraview version 5.10.0-RC1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10
name_of_file='base_case'
#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
base_casesootfoil00000vtk = FindSource(name_of_file + '.soot.foil.00000.vtk')

# set active source
SetActiveSource(base_casesootfoil00000vtk)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get display properties
base_casesootfoil00000vtkDisplay = GetDisplayProperties(base_casesootfoil00000vtk, view=renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=base_casesootfoil00000vtkDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00000vtkDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00000vtkDisplay)

# get color transfer function/color map for 'avtGhostZones'
avtGhostZonesLUT = GetColorTransferFunction('avtGhostZones')

# get opacity transfer function/opacity map for 'avtGhostZones'
avtGhostZonesPWF = GetOpacityTransferFunction('avtGhostZones')

# set scalar coloring
ColorBy(base_casesootfoil00000vtkDisplay, ('CELLS', 'Max_Normalized_Pressure'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(avtGhostZonesLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
base_casesootfoil00000vtkDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
base_casesootfoil00000vtkDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Max_Normalized_Pressure'
max_Normalized_PressureLUT = GetColorTransferFunction('Max_Normalized_Pressure')

# get opacity transfer function/opacity map for 'Max_Normalized_Pressure'
max_Normalized_PressurePWF = GetOpacityTransferFunction('Max_Normalized_Pressure')

# find source
base_casesootfoil00001vtk = FindSource(name_of_file + '.soot.foil.00001.vtk')

# set active source
SetActiveSource(base_casesootfoil00001vtk)

# get display properties
base_casesootfoil00001vtkDisplay = GetDisplayProperties(base_casesootfoil00001vtk, view=renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=base_casesootfoil00001vtkDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00001vtkDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00001vtkDisplay)

# set scalar coloring
ColorBy(base_casesootfoil00001vtkDisplay, ('CELLS', 'Max_Normalized_Pressure'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(avtGhostZonesLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
base_casesootfoil00001vtkDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
base_casesootfoil00001vtkDisplay.SetScalarBarVisibility(renderView1, True)

# find source
base_casesootfoil00002vtk = FindSource(name_of_file + '.soot.foil.00002.vtk')

# set active source
SetActiveSource(base_casesootfoil00002vtk)

# get display properties
base_casesootfoil00002vtkDisplay = GetDisplayProperties(base_casesootfoil00002vtk, view=renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=base_casesootfoil00002vtkDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00002vtkDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00002vtkDisplay)

# set scalar coloring
ColorBy(base_casesootfoil00002vtkDisplay, ('CELLS', 'Max_Normalized_Pressure'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(avtGhostZonesLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
base_casesootfoil00002vtkDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
base_casesootfoil00002vtkDisplay.SetScalarBarVisibility(renderView1, True)

# find source
base_casesootfoil00003vtk = FindSource(name_of_file + '.soot.foil.00003.vtk')

# set active source
SetActiveSource(base_casesootfoil00003vtk)

# get display properties
base_casesootfoil00003vtkDisplay = GetDisplayProperties(base_casesootfoil00003vtk, view=renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=base_casesootfoil00003vtkDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00003vtkDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00003vtkDisplay)

# set scalar coloring
ColorBy(base_casesootfoil00003vtkDisplay, ('CELLS', 'Max_Normalized_Pressure'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(avtGhostZonesLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
base_casesootfoil00003vtkDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
base_casesootfoil00003vtkDisplay.SetScalarBarVisibility(renderView1, True)

# find source
base_casesootfoil00004vtk = FindSource(name_of_file + '.soot.foil.00004.vtk')

# set active source
SetActiveSource(base_casesootfoil00004vtk)

# get display properties
base_casesootfoil00004vtkDisplay = GetDisplayProperties(base_casesootfoil00004vtk, view=renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=base_casesootfoil00004vtkDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00004vtkDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00004vtkDisplay)

# set scalar coloring
ColorBy(base_casesootfoil00004vtkDisplay, ('CELLS', 'Max_Normalized_Pressure'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(avtGhostZonesLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
base_casesootfoil00004vtkDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
base_casesootfoil00004vtkDisplay.SetScalarBarVisibility(renderView1, True)

# find source
base_casesootfoil00005vtk = FindSource(name_of_file + '.soot.foil.00005.vtk')

# set active source
SetActiveSource(base_casesootfoil00005vtk)

# get display properties
base_casesootfoil00005vtkDisplay = GetDisplayProperties(base_casesootfoil00005vtk, view=renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=base_casesootfoil00005vtkDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00005vtkDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00005vtkDisplay)

# set scalar coloring
ColorBy(base_casesootfoil00005vtkDisplay, ('CELLS', 'Max_Normalized_Pressure'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(avtGhostZonesLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
base_casesootfoil00005vtkDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
base_casesootfoil00005vtkDisplay.SetScalarBarVisibility(renderView1, True)

# find source
base_casesootfoil00006vtk = FindSource(name_of_file + '.soot.foil.00006.vtk')

# set active source
SetActiveSource(base_casesootfoil00006vtk)

# get display properties
base_casesootfoil00006vtkDisplay = GetDisplayProperties(base_casesootfoil00006vtk, view=renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=base_casesootfoil00006vtkDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00006vtkDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00006vtkDisplay)

# set scalar coloring
ColorBy(base_casesootfoil00006vtkDisplay, ('CELLS', 'Max_Normalized_Pressure'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(avtGhostZonesLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
base_casesootfoil00006vtkDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
base_casesootfoil00006vtkDisplay.SetScalarBarVisibility(renderView1, True)

# find source
base_casesootfoil00007vtk = FindSource(name_of_file + '.soot.foil.00007.vtk')

# set active source
SetActiveSource(base_casesootfoil00007vtk)

# get display properties
base_casesootfoil00007vtkDisplay = GetDisplayProperties(base_casesootfoil00007vtk, view=renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=base_casesootfoil00007vtkDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00007vtkDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00007vtkDisplay)

# set scalar coloring
ColorBy(base_casesootfoil00007vtkDisplay, ('CELLS', 'Max_Normalized_Pressure'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(avtGhostZonesLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
base_casesootfoil00007vtkDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
base_casesootfoil00007vtkDisplay.SetScalarBarVisibility(renderView1, True)

# find source
base_casesootfoil00008vtk = FindSource(name_of_file + '.soot.foil.00008.vtk')

# set active source
SetActiveSource(base_casesootfoil00008vtk)

# get display properties
base_casesootfoil00008vtkDisplay = GetDisplayProperties(base_casesootfoil00008vtk, view=renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=base_casesootfoil00008vtkDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00008vtkDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00008vtkDisplay)

# set scalar coloring
ColorBy(base_casesootfoil00008vtkDisplay, ('CELLS', 'Max_Normalized_Pressure'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(avtGhostZonesLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
base_casesootfoil00008vtkDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
base_casesootfoil00008vtkDisplay.SetScalarBarVisibility(renderView1, True)

# find source
base_casesootfoil00009vtk = FindSource(name_of_file + '.soot.foil.00009.vtk')

# set active source
SetActiveSource(base_casesootfoil00009vtk)

# get display properties
base_casesootfoil00009vtkDisplay = GetDisplayProperties(base_casesootfoil00009vtk, view=renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=base_casesootfoil00009vtkDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00009vtkDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00009vtkDisplay)

# set scalar coloring
ColorBy(base_casesootfoil00009vtkDisplay, ('CELLS', 'Max_Normalized_Pressure'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(avtGhostZonesLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
base_casesootfoil00009vtkDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
base_casesootfoil00009vtkDisplay.SetScalarBarVisibility(renderView1, True)

# find source
base_casesootfoil00010vtk = FindSource(name_of_file + '.soot.foil.00010.vtk')

# set active source
SetActiveSource(base_casesootfoil00010vtk)

# get display properties
base_casesootfoil00010vtkDisplay = GetDisplayProperties(base_casesootfoil00010vtk, view=renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=base_casesootfoil00010vtkDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00010vtkDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00010vtkDisplay)

# set scalar coloring
ColorBy(base_casesootfoil00010vtkDisplay, ('CELLS', 'Max_Normalized_Pressure'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(avtGhostZonesLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
base_casesootfoil00010vtkDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
base_casesootfoil00010vtkDisplay.SetScalarBarVisibility(renderView1, True)

# find source
base_casesootfoil00011vtk = FindSource(name_of_file + '.soot.foil.00011.vtk')

# set active source
SetActiveSource(base_casesootfoil00011vtk)

# get display properties
base_casesootfoil00011vtkDisplay = GetDisplayProperties(base_casesootfoil00011vtk, view=renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=base_casesootfoil00011vtkDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00011vtkDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00011vtkDisplay)

# set scalar coloring
ColorBy(base_casesootfoil00011vtkDisplay, ('CELLS', 'Max_Normalized_Pressure'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(avtGhostZonesLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
base_casesootfoil00011vtkDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
base_casesootfoil00011vtkDisplay.SetScalarBarVisibility(renderView1, True)

# find source
base_casesootfoil00012vtk = FindSource(name_of_file + '.soot.foil.00012.vtk')

# set active source
SetActiveSource(base_casesootfoil00012vtk)

# get display properties
base_casesootfoil00012vtkDisplay = GetDisplayProperties(base_casesootfoil00012vtk, view=renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=base_casesootfoil00012vtkDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00012vtkDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00012vtkDisplay)

# set scalar coloring
ColorBy(base_casesootfoil00012vtkDisplay, ('CELLS', 'Max_Normalized_Pressure'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(avtGhostZonesLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
base_casesootfoil00012vtkDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
base_casesootfoil00012vtkDisplay.SetScalarBarVisibility(renderView1, True)

# find source
base_casesootfoil00013vtk = FindSource(name_of_file + '.soot.foil.00013.vtk')

# set active source
SetActiveSource(base_casesootfoil00013vtk)

# get display properties
base_casesootfoil00013vtkDisplay = GetDisplayProperties(base_casesootfoil00013vtk, view=renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=base_casesootfoil00013vtkDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00013vtkDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00013vtkDisplay)

# set scalar coloring
ColorBy(base_casesootfoil00013vtkDisplay, ('CELLS', 'Max_Normalized_Pressure'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(avtGhostZonesLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
base_casesootfoil00013vtkDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
base_casesootfoil00013vtkDisplay.SetScalarBarVisibility(renderView1, True)

# find source
base_casesootfoil00014vtk = FindSource(name_of_file + '.soot.foil.00014.vtk')

# set active source
SetActiveSource(base_casesootfoil00014vtk)

# get display properties
base_casesootfoil00014vtkDisplay = GetDisplayProperties(base_casesootfoil00014vtk, view=renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=base_casesootfoil00014vtkDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00014vtkDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00014vtkDisplay)

# set scalar coloring
ColorBy(base_casesootfoil00014vtkDisplay, ('CELLS', 'Max_Normalized_Pressure'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(avtGhostZonesLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
base_casesootfoil00014vtkDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
base_casesootfoil00014vtkDisplay.SetScalarBarVisibility(renderView1, True)

# find source
base_casesootfoil00015vtk = FindSource(name_of_file + '.soot.foil.00015.vtk')

# set active source
SetActiveSource(base_casesootfoil00015vtk)

# get display properties
base_casesootfoil00015vtkDisplay = GetDisplayProperties(base_casesootfoil00015vtk, view=renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=base_casesootfoil00015vtkDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00015vtkDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00015vtkDisplay)

# set scalar coloring
ColorBy(base_casesootfoil00015vtkDisplay, ('CELLS', 'Max_Normalized_Pressure'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(avtGhostZonesLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
base_casesootfoil00015vtkDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
base_casesootfoil00015vtkDisplay.SetScalarBarVisibility(renderView1, True)

# find source
base_casesootfoil00016vtk = FindSource(name_of_file + '.soot.foil.00016.vtk')

# set active source
SetActiveSource(base_casesootfoil00016vtk)

# get display properties
base_casesootfoil00016vtkDisplay = GetDisplayProperties(base_casesootfoil00016vtk, view=renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=base_casesootfoil00016vtkDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00016vtkDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=base_casesootfoil00016vtkDisplay)

# set scalar coloring
ColorBy(base_casesootfoil00016vtkDisplay, ('CELLS', 'Max_Normalized_Pressure'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(avtGhostZonesLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
base_casesootfoil00016vtkDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
base_casesootfoil00016vtkDisplay.SetScalarBarVisibility(renderView1, True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
max_Normalized_PressureLUT.ApplyPreset('X Ray', True)

# reset view to fit data
renderView1.ResetCamera(True)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1542, 784)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [1632.0, 96.0, 6316.463653134049]
renderView1.CameraFocalPoint = [1632.0, 96.0, 0.0]
renderView1.CameraParallelScale = 921.1918815843974

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).