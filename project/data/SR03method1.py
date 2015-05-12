from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset ()
SR03method1_vtk = LegacyVTKReader( FileNames=['/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03method1.vtk'] )
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 18
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r18.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 18.2414
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r18.2414.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 18.4828
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r18.4828.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 18.7241
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r18.7241.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 18.9655
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r18.9655.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 19.2069
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r19.2069.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 19.4483
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r19.4483.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 19.6897
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r19.6897.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 19.931
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r19.931.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 20.1724
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r20.1724.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 20.4138
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r20.4138.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 20.6552
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r20.6552.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 20.8966
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r20.8966.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 21.1379
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r21.1379.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 21.3793
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r21.3793.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 21.6207
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r21.6207.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 21.8621
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r21.8621.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 22.1034
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r22.1034.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 22.3448
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r22.3448.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 22.5862
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r22.5862.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 22.8276
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r22.8276.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 23.069
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r23.069.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 23.3103
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r23.3103.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 23.5517
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r23.5517.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 23.7931
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r23.7931.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 24.0345
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r24.0345.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 24.2759
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r24.2759.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 24.5172
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r24.5172.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 24.7586
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r24.7586.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 25
Clip1.InsideOut = 1
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/radius/r25.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 0.5]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v0.5Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [0.5, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v0.5Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 0.55862]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v0.55862Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [0.55862, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v0.55862Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 0.61724]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v0.61724Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [0.61724, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v0.61724Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 0.67586]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v0.67586Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [0.67586, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v0.67586Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 0.73448]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v0.73448Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [0.73448, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v0.73448Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 0.7931]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v0.7931Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [0.7931, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v0.7931Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 0.85172]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v0.85172Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [0.85172, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v0.85172Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 0.91034]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v0.91034Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [0.91034, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v0.91034Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 0.96897]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v0.96897Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [0.96897, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v0.96897Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 1.0276]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.0276Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [1.0276, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.0276Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 1.0862]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.0862Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [1.0862, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.0862Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 1.1448]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.1448Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [1.1448, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.1448Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 1.2034]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.2034Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [1.2034, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.2034Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 1.2621]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.2621Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [1.2621, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.2621Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 1.3207]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.3207Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [1.3207, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.3207Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 1.3793]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.3793Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [1.3793, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.3793Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 1.4379]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.4379Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [1.4379, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.4379Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 1.4966]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.4966Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [1.4966, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.4966Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 1.5552]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.5552Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [1.5552, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.5552Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 1.6138]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.6138Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [1.6138, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.6138Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 1.6724]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.6724Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [1.6724, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.6724Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 1.731]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.731Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [1.731, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.731Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 1.7897]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.7897Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [1.7897, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.7897Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 1.8483]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.8483Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [1.8483, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.8483Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 1.9069]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.9069Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [1.9069, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.9069Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 1.9655]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.9655Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [1.9655, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v1.9655Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 2.0241]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v2.0241Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [2.0241, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v2.0241Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 2.0828]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v2.0828Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [2.0828, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v2.0828Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 2.1414]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v2.1414Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [2.1414, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v2.1414Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
Clip1 = Clip(ClipType="Sphere")
Clip1.ClipType.Center = [0.0, 0.0, 0.0]
Clip1.ClipType.Radius = 16.6
Clip1.InsideOut = 1
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [-100.0, 2.2]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v2.2Part1.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
Delete (Clip1)
SetActiveSource(SR03method1_vtk)
IsoVolume1 = IsoVolume()
IsoVolume1.InputScalars = ['POINTS','uz']
IsoVolume1.ThresholdRange = [2.2, 100.0]
integrateVariables1 = IntegrateVariables()
SpreadSheetView1 = CreateView("SpreadSheetView")
DataRepresentation = Show()
Render()
writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/SR03/method1/velocity/v2.2Part2.csv")
writer.Precision = 8
writer.UseScientificNotation = 1
writer.FieldAssociation = "Points"
writer.UpdatePipeline()
del writer
Delete (SpreadSheetView1)
Delete (integrateVariables1)
Delete (IsoVolume1)
SetActiveSource(SR03method1_vtk)
