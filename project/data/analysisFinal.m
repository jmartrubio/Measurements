clear all;
clc;
close all;

cd ~/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/
calculateThings = 0;
saveVTK = 1;
createScript = 1;

%First of all, center of the actual cylinder was found to be a little
%deviated from the actual (0, 0) coordinate. I modify coords to adjust them
caso = 'SR05';
method = '2';

if calculateThings
center= calculatedCenter(caso,method);
radius = linspace(18,25,30);
velocities = linspace(0.5,2.2,30);

% Loading data
data = load (strcat(caso,'.dat'));
x=data(:,1) -center(1);
y=data(:,2) -center(2);
u=data(:,3);
v=data(:,4);
w=data(:,5);


% Cleaning data for proper matrix representation
Y = y(1:58)';
X = limpia(x);

[Xgrid, Ygrid] = meshgrid(X, Y);

Umatrix = makematrix(u);
Vmatrix = makematrix(v);
Wmatrix = makematrix(w);


% Representation of Velocity vectors, and contours
% figVec = representaVec(Xgrid,Ygrid,Umatrix,Vmatrix);
% representa(Xgrid,Ygrid,Umatrix,Vmatrix,Wmatrix,'Ux','Uy','Uz');


% Now calculating radial and tangential velocity
for i=1:length(x)
    r(i)=sqrt(x(i)^2 + y(i)^2);
    phi(i)=atan2(y(i),x(i));
    ur(i)=u(i)*cos(phi(i))+v(i)*sin(phi(i));
    uphi(i)=-u(i)*sin(phi(i))+v(i)*cos(phi(i));   
    var1(i) = w(i)*uphi(i)*r(i);
    var2(i) = w(i)*w(i)- 0.5 *uphi(i)*uphi(i);
end

% Creating matrix representation of data
Phimatrix = makematrix(phi);
URmatrix = makematrix(ur);
UPHImatrix = makematrix(uphi);
VAR1matrix = makematrix(var1);
VAR2matrix = makematrix(var2);

%Contour representation of velocity in cilindrical coords
% representa(Xgrid,Ygrid,URmatrix,UPHImatrix,Wmatrix,'Ur','Uphi','Uz');

% 2D representation cyl coords
% fig2D = representa2D(r,ur,uphi,w);

%Saving vtk file to open it in paraview

if saveVTK
    savevtkWithVarI(X,Y,Umatrix,Vmatrix,Wmatrix,URmatrix,strcat(caso,'method',method),VAR1matrix,VAR2matrix);
end


%Now we create paraview scripting profiles
if createScript == 1

    pythonScript = fopen(strcat(caso,'method',method,'.py'),'w');
    fprintf(pythonScript,'from paraview.simple import *\n');
    fprintf(pythonScript,'paraview.simple._DisableFirstRenderCameraReset ()\n');
    fprintf(pythonScript,strcat(caso,'method',method,'_vtk = LegacyVTKReader( FileNames=[\''/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/',caso,'method',method,'.vtk\''] )\n'));

    
    %First of all we do all the clippings with sphere to determine the
    %radius analysis, We should in here calculate the integral of Uz for
    %the mass and the integral of Int1 Int2 for the Swirl. All those
    %variables (Uz, var1, var2) should be stored in th vtk already
    for rad = 1:length(radius)
        fprintf(pythonScript,'Clip1 = Clip(ClipType="Sphere")\n');
        fprintf(pythonScript,'Clip1.ClipType.Center = [0.0, 0.0, 0.0]\n');
        fprintf(pythonScript,strcat('Clip1.ClipType.Radius =',32,num2str(radius(rad)),'\n'));
        fprintf(pythonScript,'Clip1.InsideOut = 1\n');
        fprintf(pythonScript,'integrateVariables1 = IntegrateVariables()\n');
        fprintf(pythonScript,'SpreadSheetView1 = CreateView("SpreadSheetView")\n');
        fprintf(pythonScript,'DataRepresentation = Show()\n');
        fprintf(pythonScript,'Render()\n');
        fprintf(pythonScript,strcat('writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/',caso,'/method',method,'/radius/r',num2str(radius(rad)),'.csv")\n'));
        fprintf(pythonScript,'writer.Precision = 8\n');
        fprintf(pythonScript,'writer.UseScientificNotation = 1\n');
        fprintf(pythonScript,'writer.FieldAssociation = "Points"\n');
        fprintf(pythonScript,'writer.UpdatePipeline()\n');
        fprintf(pythonScript,'del writer\n');
        fprintf(pythonScript,'Delete (SpreadSheetView1)\n');
        fprintf(pythonScript,'Delete (integrateVariables1)\n');
        fprintf(pythonScript,'Delete (Clip1)\n');
        fprintf(pythonScript,strcat('SetActiveSource(',caso,'method',method,'_vtk)\n'));
    end    
    %Now we write the code to perform the similar analysis but with the
    %limited velocity in axial direction
    
    
   for vel = 1:length(velocities)
        fprintf(pythonScript,'Clip1 = Clip(ClipType="Sphere")\n');
        fprintf(pythonScript,'Clip1.ClipType.Center = [0.0, 0.0, 0.0]\n');
        fprintf(pythonScript,strcat('Clip1.ClipType.Radius = 16.6\n'));
        fprintf(pythonScript,'Clip1.InsideOut = 1\n');
        fprintf(pythonScript,'IsoVolume1 = IsoVolume()\n');
        fprintf(pythonScript,'IsoVolume1.InputScalars = [\''POINTS\'',\''uz\'']\n');
        fprintf(pythonScript,strcat('IsoVolume1.ThresholdRange = [-100.0',',',32,num2str(velocities(vel)),']\n'));
        fprintf(pythonScript,'integrateVariables1 = IntegrateVariables()\n');
        fprintf(pythonScript,'SpreadSheetView1 = CreateView("SpreadSheetView")\n');
        fprintf(pythonScript,'DataRepresentation = Show()\n');
        fprintf(pythonScript,'Render()\n');
        fprintf(pythonScript,strcat('writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/',caso,'/method',method,'/velocity/v',num2str(velocities(vel)),'Part1.csv")\n'));
        fprintf(pythonScript,'writer.Precision = 8\n');
        fprintf(pythonScript,'writer.UseScientificNotation = 1\n');
        fprintf(pythonScript,'writer.FieldAssociation = "Points"\n');
        fprintf(pythonScript,'writer.UpdatePipeline()\n');
        fprintf(pythonScript,'del writer\n');
        fprintf(pythonScript,'Delete (SpreadSheetView1)\n');
        fprintf(pythonScript,'Delete (integrateVariables1)\n');
        fprintf(pythonScript,'Delete (IsoVolume1)\n');
        fprintf(pythonScript,'Delete (Clip1)\n');
        fprintf(pythonScript,strcat('SetActiveSource(',caso,'method',method,'_vtk)\n'));
        fprintf(pythonScript,'IsoVolume1 = IsoVolume()\n');
        fprintf(pythonScript,'IsoVolume1.InputScalars = [\''POINTS\'',\''uz\'']\n');
        fprintf(pythonScript,strcat('IsoVolume1.ThresholdRange = [',num2str(velocities(vel)),',',32,'100.0]\n'));
        fprintf(pythonScript,'integrateVariables1 = IntegrateVariables()\n');
        fprintf(pythonScript,'SpreadSheetView1 = CreateView("SpreadSheetView")\n');
        fprintf(pythonScript,'DataRepresentation = Show()\n');
        fprintf(pythonScript,'Render()\n');
        fprintf(pythonScript,strcat('writer = CreateWriter("/home/javier/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/',caso,'/method',method,'/velocity/v',num2str(velocities(vel)),'Part2.csv")\n'));
        fprintf(pythonScript,'writer.Precision = 8\n');
        fprintf(pythonScript,'writer.UseScientificNotation = 1\n');
        fprintf(pythonScript,'writer.FieldAssociation = "Points"\n');
        fprintf(pythonScript,'writer.UpdatePipeline()\n');
        fprintf(pythonScript,'del writer\n');       
        fprintf(pythonScript,'Delete (SpreadSheetView1)\n');
        fprintf(pythonScript,'Delete (integrateVariables1)\n');
        fprintf(pythonScript,'Delete (IsoVolume1)\n'); 
        fprintf(pythonScript,strcat('SetActiveSource(',caso,'method',method,'_vtk)\n'));
    
   end
    
    
    fclose(pythonScript);
    
end

else
    
% Now let's try to load all the data we have generated
  



end




%%
% With Paraview mass flow can easily be calculated several ways. 
% Since rho is not known i express it in L/min
% Mass flow is determined as rho * UzMean * S [kg/s], WE CHANGE UNITS
disp ('MASS FLOW [L/min] CONSIDERING FIXED CIRCLES'); %Calculated with circles centered in 0 0
disp ('Radius           18mm        19mm        20mm        21mm        22mm        23mm        24mm        25mm')
disp (strcat('Mass flow',' ' ,32,32,32,32,num2str(8014.97/1000*60),32,32,32,32,num2str(8773.04/1000*60),32,32,32,32,num2str(9129.53/1000*60),32,32,32,32,num2str(9256.82/1000*60),32,32,32,32,num2str(9320.72/1000*60),32,32,32,32,num2str(9374.26/1000*60),32,32,32,32,num2str(9426.63/1000*60),32,32,32,32,num2str(9478.27/1000*60)));
disp('----------------------------------------');
% Calculated with a treshold value of velocity
disp ('MASS FLOW [L/min] CONSIDERING FIXED Z VELOCITY');
disp ('zVelocity      0.5m/s      0.6m/s      0.7m/s      0.8m/s      0.9m/s    1.0m/s      1.1m/s      1.2m/s')
disp (strcat('Mass flow',32,32,32,32,num2str(9275.17/1000*60),32,32,32,32,num2str(9252.73/1000*60),32,32,32,32,num2str(9234.24/1000*60),32,32,32,32,num2str(9218.16/1000*60),32,32,32,32,num2str(9205.82/1000*60),32,32,32,32,num2str(9194.5/1000*60),32,32,32,32,num2str(9183.21/1000*60),32,32,32,32,num2str(9172.17/1000*60)));
disp('----------------------------------------');
% Calculation of swirl number:
% There are several definition. First attemp will be just considering the
% mean fluxes in num and denom (see formula). That corresponds to a
% surface integral Int1 = surfaceInt(var1) and Int2=surfaceInt(var2), where
% S =  Int1/(Rref Int2)
% var1 and var2 are calculated in paraview and results are different for
% several maximum radius considered in the calculation from 18 to 25mm
Rref=18;% (All variables are storaged in mm)
disp ('SWIRL NUMBER DIFFERENT CIRCLES'); %Calculated with circles centered in 0 0
disp ('Radius           18mm       19mm       20mm       21mm      22mm       23mm       24mm       25mm')
disp (strcat('SwirlNumber',32,32,32,32,num2str(831580/71020.2/Rref),32,32,32,32,num2str(915086/76369.7/Rref),32,32,32,32,num2str(938161/77745.4/Rref),32,32,32,32,num2str(942108/77965.1/Rref),32,32,32,32,num2str(942833/78003.6/Rref),32,32,32,32,num2str(943236/78024.5/Rref),32,32,32,32,num2str(943622/78043.4/Rref),32,32,32,32,num2str(944014/78061/Rref)));

% We could compare the values to those obtained from calculations only in
% lines, in four possibilities x=0+ x=0- y=0+ y=0-


disp('----------------------------------------');
disp('----------------------------------------');

%Case 1 on y=0: from x=0 to x=30
r1=X(29:59);
uphi1=UPHImatrix(31,29:59);
uz1=Wmatrix(31,29:59);
figure;
plot(r1,uphi1,'r'); hold on;
plot (r1,uz1,'b');
disp ('SWIRL NUMBER DIFFERENT CIRCLES case1'); %Calculated with circles centered in 0 0
disp ('Radius           18mm       19mm       20mm       21mm      22mm       23mm       24mm       25mm')
disp (strcat('SwirlNumber',32,32,32,32,num2str(S(uz1,uphi1,r1,18,Rref)),32,32,32,32,num2str(S(uz1,uphi1,r1,19,Rref)),32,32,32,32,num2str(S(uz1,uphi1,r1,20,Rref)),32,32,32,32,num2str(S(uz1,uphi1,r1,21,Rref)),32,32,32,32,num2str(S(uz1,uphi1,r1,22,Rref)),32,32,32,32,num2str(S(uz1,uphi1,r1,23,Rref)),32,32,32,32,num2str(S(uz1,uphi1,r1,24,Rref)),32,32,32,32,num2str(S(uz1,uphi1,r1,25,Rref))));

disp('----------------------------------------');
%Case 2 on y=0: from x=-30 to x=0
r2=-(X(1:28));
uphi2=UPHImatrix(31,1:28);
uz2=Wmatrix(31,1:28);
figure;
plot(r2,uphi2,'r'); hold on;
plot (r2,uz2,'b');
disp ('SWIRL NUMBER DIFFERENT CIRCLES case2'); %Calculated with circles centered in 0 0
disp ('Radius           18mm       19mm       20mm       21mm      22mm       23mm       24mm       25mm')
disp (strcat('SwirlNumber',32,32,32,32,num2str(S(uz2,uphi2,r2,18,Rref)),32,32,32,32,num2str(S(uz2,uphi2,r2,19,Rref)),32,32,32,32,num2str(S(uz2,uphi2,r2,20,Rref)),32,32,32,32,num2str(S(uz2,uphi2,r2,21,Rref)),32,32,32,32,num2str(S(uz2,uphi2,r2,22,Rref)),32,32,32,32,num2str(S(uz2,uphi2,r2,23,Rref)),32,32,32,32,num2str(S(uz2,uphi2,r2,24,Rref)),32,32,32,32,num2str(S(uz2,uphi2,r2,25,Rref))));
disp('----------------------------------------');
%Case 3 on x=0: from y=0 to y=30
r3=(Y(31:58));
uphi3=UPHImatrix(31:58,29);
uz3=Wmatrix(31:58,29);
figure;
plot(r3,uphi3,'r'); hold on;
plot (r3,uz3,'b');
disp ('SWIRL NUMBER DIFFERENT CIRCLES case3'); %Calculated with circles centered in 0 0
disp ('Radius           18mm       19mm       20mm       21mm      22mm       23mm       24mm       25mm')
disp (strcat('SwirlNumber',32,32,32,32,num2str(S(uz3,uphi3,r3,18,Rref)),32,32,32,32,num2str(S(uz3,uphi3,r3,19,Rref)),32,32,32,32,num2str(S(uz3,uphi3,r3,20,Rref)),32,32,32,32,num2str(S(uz3,uphi3,r3,21,Rref)),32,32,32,32,num2str(S(uz3,uphi3,r3,22,Rref)),32,32,32,32,num2str(S(uz3,uphi3,r3,23,Rref)),32,32,32,32,num2str(S(uz3,uphi3,r3,24,Rref)),32,32,32,32,num2str(S(uz3,uphi3,r3,25,Rref))));
disp('----------------------------------------');
%Case 4 on x=0: from y=0 to y=30
r4=-(Y(1:30));
uphi4=UPHImatrix(1:30,29);
uz4=Wmatrix(1:30,29);
figure;
plot(r4,uphi4,'r'); hold on;
plot (r4,uz4,'b');
disp ('SWIRL NUMBER DIFFERENT CIRCLES case4'); %Calculated with circles centered in 0 0
disp ('Radius           18mm       19mm       20mm       21mm      22mm       23mm       24mm       25mm')
disp (strcat('SwirlNumber',32,32,32,32,num2str(S(uz4,uphi4,r4,18,Rref)),32,32,32,32,num2str(S(uz4,uphi4,r4,19,Rref)),32,32,32,32,num2str(S(uz4,uphi4,r4,20,Rref)),32,32,32,32,num2str(S(uz4,uphi4,r4,21,Rref)),32,32,32,32,num2str(S(uz4,uphi4,r4,22,Rref)),32,32,32,32,num2str(S(uz4,uphi4,r4,23,Rref)),32,32,32,32,num2str(S(uz4,uphi4,r4,24,Rref)),32,32,32,32,num2str(S(uz4,uphi4,r4,25,Rref))));
disp('----------------------------------------');
disp('----------------------------------------');
%Mean of the four cases
disp ('SWIRL NUMBER DIFFERENT CIRCLES Mean'); %Calculated with circles centered in 0 0
disp ('Radius           18mm       19mm       20mm       21mm      22mm       23mm       24mm       25mm')
disp (strcat('SwirlNumber',32,32,32,32,num2str(0.25*(S(uz1,uphi1,r1,18,Rref)+S(uz2,uphi2,r2,18,Rref)+S(uz3,uphi3,r3,18,Rref)+S(uz4,uphi4,r4,18,Rref))),32,32,32,32,num2str(0.25*(S(uz1,uphi1,r1,19,Rref)+S(uz2,uphi2,r2,19,Rref)+S(uz3,uphi3,r3,19,Rref)+S(uz4,uphi4,r4,19,Rref))),32,32,32,32,num2str(0.25*(S(uz1,uphi1,r1,20,Rref)+S(uz2,uphi2,r2,20,Rref)+S(uz3,uphi3,r3,20,Rref)+S(uz4,uphi4,r4,20,Rref))),32,32,32,32,num2str(0.25*(S(uz1,uphi1,r1,21,Rref)+S(uz2,uphi2,r2,21,Rref)+S(uz3,uphi3,r3,21,Rref)+S(uz4,uphi4,r4,21,Rref))),32,32,32,32,num2str(0.25*(S(uz1,uphi1,r1,22,Rref)+S(uz2,uphi2,r2,22,Rref)+S(uz3,uphi3,r3,22,Rref)+S(uz4,uphi4,r4,22,Rref))),32,32,32,32,num2str(0.25*(S(uz1,uphi1,r1,23,Rref)+S(uz2,uphi2,r2,23,Rref)+S(uz3,uphi3,r3,23,Rref)+S(uz4,uphi4,r4,23,Rref))),32,32,32,32,num2str(0.25*(S(uz1,uphi1,r1,24,Rref)+S(uz2,uphi2,r2,24,Rref)+S(uz3,uphi3,r3,24,Rref)+S(uz4,uphi4,r4,24,Rref))),32,32,32,32,num2str(0.25*(S(uz1,uphi1,r1,25,Rref)+S(uz2,uphi2,r2,25,Rref)+S(uz3,uphi3,r3,25,Rref)+S(uz4,uphi4,r4,25,Rref)))));
