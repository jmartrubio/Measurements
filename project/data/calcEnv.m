function [renMin,renMax, urenMin, urenMax] = calcEnv(r,ur,dista)
m=1;


for i=1:length(r)
    if ((r(i)<28) || (abs(ur(i))>1e-4))
        rnew(m)=r(i);
        urnew(m)=ur(i);
        m=m+1;
    end
end


clear r ur;
r=rnew;
ur = urnew;

%Divides r range into n intervals of "dist" distance, for each determines
%the maximum value of velociy and assigns the value to ren urenMax

n = round(max(r)/dista);

l=1;
q=1;
maxi = -2;
mini = 15;
rInter(1)=0;
for i=1:n
    rInter(i+1)=max(r)/n * i;
    for j=1:length(r)
        if (r(j)<((max(r)/n)*i)) &&  (r(j)>((max(r)/n)*(i-1)))
            if ur(j)>maxi
                urenMax(q)=ur(j);
                renMax(q)=r(j);
                maxi=ur(j);
            end
            if ur(j)<mini
                urenMin(l)=ur(j);
                renMin(l)=r(j);
                mini=ur(j);
            end
        end
    end
    maxi = -2;
    mini = 15;
    q=q+1;
    l=l+1;
end