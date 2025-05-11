# trace generated using paraview version 5.10.0-RC1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

name_of_file='Epsilon_9_Q_50_G_1.2'
number_of_files=17

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
source = FindSource(name_of_file + '.soot.foil.00000.vtk')

# set active source
SetActiveSource(source)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get display properties
source_Display = GetDisplayProperties(source, view=renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=source_Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=source_Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=source_Display)

# get color transfer function/color map for 'avtGhostZones'
avtGhostZonesLUT = GetColorTransferFunction('avtGhostZones')

# get opacity transfer function/opacity map for 'avtGhostZones'
avtGhostZonesPWF = GetOpacityTransferFunction('avtGhostZones')

# set scalar coloring
ColorBy(source_Display, ('CELLS', 'Max_Normalized_Pressure'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(avtGhostZonesLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
source_Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
source_Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Max_Normalized_Pressure'
max_Normalized_PressureLUT = GetColorTransferFunction('Max_Normalized_Pressure')

# get opacity transfer function/opacity map for 'Max_Normalized_Pressure'
max_Normalized_PressurePWF = GetOpacityTransferFunction('Max_Normalized_Pressure')

for i in range(1, number_of_files):
    if i < 10:
        # find source
        source = FindSource(name_of_file + '.soot.foil.0000' + str(i) + '.vtk')
        
        # set active source
        SetActiveSource(source)

        # get display properties
        source_Display = GetDisplayProperties(source, view=renderView1)

        # toggle 3D widget visibility (only when running from the GUI)
        Show3DWidgets(proxy=source_Display)

        # toggle 3D widget visibility (only when running from the GUI)
        Hide3DWidgets(proxy=source_Display.SliceFunction)

        # toggle 3D widget visibility (only when running from the GUI)
        Hide3DWidgets(proxy=source_Display)

        # set scalar coloring
        ColorBy(source_Display, ('CELLS', 'Max_Normalized_Pressure'))

        # Hide the scalar bar for this color map if no visible data is colored by it.
        HideScalarBarIfNotNeeded(avtGhostZonesLUT, renderView1)

        # rescale color and/or opacity maps used to include current data range
        source_Display.RescaleTransferFunctionToDataRange(True, False)

        # show color bar/color legend
        source_Display.SetScalarBarVisibility(renderView1, True)
    else:
                # find source
        source = FindSource(name_of_file + '.soot.foil.000' + str(i) + '.vtk')
        
        # set active source
        SetActiveSource(source)

        # get display properties
        source_Display = GetDisplayProperties(source, view=renderView1)

        # toggle 3D widget visibility (only when running from the GUI)
        Show3DWidgets(proxy=source_Display)

        # toggle 3D widget visibility (only when running from the GUI)
        Hide3DWidgets(proxy=source_Display.SliceFunction)

        # toggle 3D widget visibility (only when running from the GUI)
        Hide3DWidgets(proxy=source_Display)

        # set scalar coloring
        ColorBy(source_Display, ('CELLS', 'Max_Normalized_Pressure'))

        # Hide the scalar bar for this color map if no visible data is colored by it.
        HideScalarBarIfNotNeeded(avtGhostZonesLUT, renderView1)

        # rescale color and/or opacity maps used to include current data range
        source_Display.RescaleTransferFunctionToDataRange(True, False)

        # show color bar/color legend
        source_Display.SetScalarBarVisibility(renderView1, True)


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