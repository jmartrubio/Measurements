% Save MATLAB variables in VTK format
% x is a list of points
% y is a list of values in the x points
% VarName is the Variable Name
%
%  Example:
%
%  mtst=[11 12 13 14; 21 22 23 24];
%  [sy,sx]=size(mtst);
%  savevtk_xyv(1:sx,1:sy,mtst,mtst,'2DVectors');
%
% Coded by Sebastian Jardi Estadella
% http://www.tinet.org/~sje/index_en.htm
%

function [fd,err]=savevtk(x,y,vx,vy,vz,VarName,alpha)

nx=length(x);
ny=length(y);
[nfvx,ncvx]=size(vx); % number of rows and columns
[nfvy,ncvy]=size(vy);
[nfvz,ncvz]=size(vy);

if nx~=ncvx 
  disp('length(x) and ncvx have to be equals.');
  disp(nx);
  disp(ncvx);
  return;
end

if nx~=ncvy 
  disp('length(x) and ncvy have to be equals.');
  disp(nx);
  disp(ncvy);
  return;
end

if ny~=nfvx 
  disp('length(x) and nfvx have to be equals.');
  disp(ny);
  disp(nfvx);
  return;
end

if ny~=nfvy 
  disp('length(x) and nfvy have to be equals.');
  disp(ny);
  disp(nfvy);
  return;
end


filename=sprintf('%s.vtk',VarName);

fd=fopen(filename,'w');		% Open for write, created file if required
									% and deletes previous contents.

fprintf(fd,'# vtk DataFile Version 2.0\n');
err=fclose(fd);                           

fd=fopen(filename,'a');     % Opens the file to Append.

fprintf(fd,'Structured Grid\n');
fprintf(fd,'ASCII\n');
fprintf(fd,'\n');
fprintf(fd,'DATASET RECTILINEAR_GRID\n');
fprintf(fd,'DIMENSIONS %d %d %d\n',nx,ny,1);

fprintf(fd,'X_COORDINATES %d double\n',nx);
for i=1:nx
  fprintf(fd,'%f\n',x(i));  
end
fprintf(fd,'\n');

fprintf(fd,'Y_COORDINATES %d double\n',ny);
for i=1:ny
  fprintf(fd,'%f\n',y(i));  
end
fprintf(fd,'\n');

fprintf(fd,'Z_COORDINATES 1 double\n');
fprintf(fd,'0 \n');

fprintf(fd,'\n');
fprintf(fd,'POINT_DATA %d\n',nx*ny);
fprintf(fd,'SCALARS alpha double\n');
fprintf(fd,'LOOKUP_TABLE default\n');
for i_f=1:nfvx
  for i_c=1:ncvx
    fprintf(fd,'%f\n',alpha(i_f,i_c));  
  end
end
fprintf(fd,'\n');
fprintf(fd,'VECTORS ');
fprintf(fd,VarName);
fprintf(fd,' double\n');
for i_f=1:nfvx
  for i_c=1:ncvx
    fprintf(fd,'%f %f %f\n',vx(i_f,i_c),vy(i_f,i_c),vz(i_f,i_c));  
  end
end
fprintf(fd,'\n');

err=fclose(fd);

