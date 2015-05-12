function figVec =representaVec(Xgrid,Ygrid,Umatrix,Vmatrix)

figVec = figure();
quiverwcolorbar(Xgrid,Ygrid,Umatrix,Vmatrix);

caxis ([0,2.5]);
xlim([-30,30]);
ylim([-30,30]);
xlabel('x [mm]');
ylabel('y [mm]');
title ('Vector plot');
view([0 ,0,-10]);