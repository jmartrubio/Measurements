function fig2D = representa2D(r,ur,uphi,uz)

fig2D = figure();
plot(r,ur,'+r'); hold on;
plot(r,uphi,'*b'); hold on;
plot (r,uz,'sk');
legend('Ur [m/s]','Uphi [m/s]','Uz [m/s]');
xlabel ('r [mm]');
ylabel ('Velocity [m/s]');
title ('Velocity components');