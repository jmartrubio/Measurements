function representa(Xgrid,Ygrid,Umatrix,Vmatrix,Wmatrix,U1,U2,U3)


figure('Position',[120,120,1500,800]);

subplot(2,3,1);
surf(Xgrid,Ygrid,Umatrix)
xlabel('x [mm]');
ylabel('y [mm]');
title (strcat(U1,' velocity'));
view([0 ,0,10]);
axis equal
xlim([min(Xgrid(1,:)),max(Xgrid(1,:))]);
ylim([min(Ygrid(:,1)),max(Ygrid(:,1))]);
colorbar;
% caxis ([-2,2]);




subplot(2,3,2);
surf(Xgrid,Ygrid,Vmatrix)
xlabel('x [mm]');
ylabel('y [mm]');
title (strcat(U2,' velocity'));
view([0,0,10]);
axis equal
xlim([min(Xgrid(1,:)),max(Xgrid(1,:))]);
ylim([min(Ygrid(:,1)),max(Ygrid(:,1))]);
colorbar;

% caxis ([-2,2]);

subplot(2,3,3);
surf(Xgrid,Ygrid,Wmatrix)
view([0 ,0,10]);
xlabel('x [mm]');
ylabel('y [mm]');
title (strcat(U3,' velocity'));
axis equal
xlim([min(Xgrid(1,:)),max(Xgrid(1,:))]);
ylim([min(Ygrid(:,1)),max(Ygrid(:,1))]);
colorbar;
% caxis ([-1,12]);




subplot(2,3,4);
contour(Xgrid,Ygrid,Umatrix)
xlabel('x [mm]');
ylabel('y [mm]');
title (strcat(U1,' velocity'));
view([0 ,0,10]);
axis equal
xlim([min(Xgrid(1,:)),max(Xgrid(1,:))]);
ylim([min(Ygrid(:,1)),max(Ygrid(:,1))]);
colorbar;
% caxis ([-2,2]);




subplot(2,3,5);
contour(Xgrid,Ygrid,Vmatrix)
xlabel('x [mm]');
ylabel('y [mm]');
title (strcat(U2,' velocity'));
view([0,0,10]);
axis equal
xlim([min(Xgrid(1,:)),max(Xgrid(1,:))]);
ylim([min(Ygrid(:,1)),max(Ygrid(:,1))]);
colorbar;

% caxis ([-2,2]);

subplot(2,3,6);
contour(Xgrid,Ygrid,Wmatrix)
view([0 ,0,10]);
xlabel('x [mm]');
ylabel('y [mm]');
title (strcat(U3,' velocity'));
axis equal
xlim([min(Xgrid(1,:)),max(Xgrid(1,:))]);
ylim([min(Ygrid(:,1)),max(Ygrid(:,1))]);
colorbar;
% caxis ([-1,12]);