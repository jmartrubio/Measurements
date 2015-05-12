% clc;
clear all;
close all;

cd ~/OpenFOAM/javier-2.3.x/courses/Measurements/project/data/
method = '2';
% 1.- Calculated with lines intersection
% 2.- Calculated minimizing angular momentum

%First of all, center of the actual cylinder was found to be a little
%deviated from the actual (0, 0) coordinate. I modify coords to adjust them

% Loading data
plotAll=0;
files = {'SR03','SR04','SR05'};
% files = {'SR03'};%,'SR04','SR05'};

for i=1:length(files) % If first method is chosen, SR...vtk is saved to operate with paraview
    
    data = load (strcat(files{i},'.dat'));

            x0=data(:,1);
            y0=data(:,2);
            u0=data(:,3);
            v0=data(:,4);
            w0=data(:,5);

            Y0 = y0(1:58)';
            X0 = limpia(x0);

            [X0grid, Y0grid] = meshgrid(X0, Y0);

            U0matrix = makematrix(u0);
            V0matrix = makematrix(v0);
            W0matrix = makematrix(w0);
            
  if plotAll
            representa(X0grid,Y0grid,U0matrix,V0matrix,W0matrix,'Ux','Uy','Uz');
            
            figVec = representaVec(X0grid,Y0grid,U0matrix,V0matrix);
            figure(figVec);
  else
      if method == '1'
          figure();
      end
  end
  
switch method
       
    case {'1'}
        
            figure();

            [a0,b0]=contour(X0grid,Y0grid,U0matrix,[0 0]);hold on
            ax=a0(1,2:length(a0(1,:)));
            ay=a0(2,2:length(a0(1,:)));
            [a1,b1]=contour(X0grid,Y0grid,V0matrix,[0 0]);
            bx=a1(1,2:length(a1(1,:)));
            by=a1(2,2:length(a1(1,:)));
            [a2,b2]=contour(X0grid,Y0grid,U0matrix+V0matrix,[0 0]); 
            cx=a2(1,2:length(a2(1,:)));
            cy=a2(2,2:length(a2(1,:)));          
            [a3,b3]=contour(X0grid,Y0grid,U0matrix-V0matrix,[0 0]);   
            dx=a3(1,2:length(a3(1,:)));
            dy=a3(2,2:length(a3(1,:)));

            axis equal;
            
            figure;
            plot(bx,by); hold on;
            plot(ax,ay);
            plot(cx,cy);
            plot(dx,dy);
            axis equal;
            
            
            [ax,ay]=reduceVector(ax,ay,-8,4.8);
            [bx,by]=reduceVector(bx,by,-8,4.8);
            [cx,cy]=reduceVector(cx,cy,-8,4.8);
            [dx,dy]=reduceVector(dx,dy,-8,4.8);
            
            plot(ax,ay,'r'); hold on;    
            plot(bx,by,'r'); 
            plot(cx,cy,'r');
            plot(dx,dy,'r');
            
            %Calculating intersectionPoints
            % p1 intersect a b
            % p2 intersect a c
            % p3 intersect a d
            % p4 intersect b c
            % p5 intersect b d
            
            
            [p1.x p1.y]=intersections(ax,ay,bx,by,1);
            [p2.x p2.y]=intersections(ax,ay,cx,cy,1);
            [p3.x p3.y]=intersections(ax,ay,dx,dy,1);
            [p4.x p4.y]=intersections(bx,by,cx,cy,1);           
            [p5.x p5.y]=intersections(bx,by,dx,dy,1);
            
            plot(p1.x,p1.y,'xk','Markersize',10);
            plot(p2.x,p2.y,'xk','Markersize',10);
            plot(p3.x,p3.y,'xk','Markersize',10);
            plot(p4.x,p4.y,'xk','Markersize',10);
            plot(p5.x,p5.y,'xk','Markersize',10);
            [center,radius]=minboundcircle([p1.x p2.x p3.x p4.x p5.x], [p1.y  p2.y p3.y  p4.y p5.y],true);
            circle(center(1),center(2),radius);
            
            disp(strcat('Centered determined for case',32,files{i},32,'with method',32,method,':'));
            disp(center);
%             savevtkNoPhi(X0,Y0,U0matrix,V0matrix,W0matrix,strcat('U',files{i}));
      
    
    case {'2'}
        

       
            
            %normAngMom([0 0],x0,y0,u0,v0)
            options = optimset('TolX',1e-50,'TolFun',1e-50,'MaxIter',10000000,'MaxFunEvals',10000000);
            [center,fval]=fminsearch(@(c) normAngMom(c,x0,y0,u0,v0),[0, 0],options);
            
            disp(strcat('Centered determined for case',32,files{i},32,'with method',32,method,':'));
            disp(center);
            
end
end