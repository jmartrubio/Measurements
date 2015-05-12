clear all;
clc;
% close all;

cd ~/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/
saveVTK = 0;
displX = [ -1.198795553691046  ];
displY =  -0.050637582815586;
%First of all, center of the actual cylinder was found to be a little
%deviated from the actual (0, 0) coordinate. I modify coords to adjust them

for mm=1:length(displX)

data = load ('SR03.dat');
x=data(:,1) -displX(mm);
y=data(:,2) -displY;
u=data(:,3);
v=data(:,4);
w=data(:,5);



% Now calculating radial and tangential velocity
for i=1:length(x)
    r(i)=sqrt(x(i)^2 + y(i)^2);
    phi(i)=atan2(y(i),x(i));
    ur(i)=u(i)*cos(phi(i))+v(i)*sin(phi(i));
    uphi(i)=-u(i)*sin(phi(i))+v(i)*cos(phi(i));   
end


% 2D representation cyl coords
representa2D(r,ur,uphi,w);
title (num2str(displX(mm)));

end
