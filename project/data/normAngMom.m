function f = normAngMom(c,x,y,u,v)

xprim = x-c(1);
yprim = y-c(2);

sum = 0;
for i=1:length(xprim)
    r(i)=sqrt(xprim(i)^2 + yprim(i)^2);
    phi(i)=atan2(yprim(i),xprim(i));
%     ur(i)=u(i)*cos(phi(i))+v(i)*sin(phi(i));
    uphi(i)=-u(i)*sin(phi(i))+v(i)*cos(phi(i));   
    sum=sum + uphi(i)/(sqrt(u(i)^2 + v(i)^2)+1e-50); 
end

f = -sum/length(x);

    
%Function that calculates the value of normalized angular momentum (changed sign so as to find the minimum)