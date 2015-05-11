function S = S(uz,uphi,r,rlim,Rref)
q=1;
for i=1:length(r)
    if r(i)<rlim
       
        rnew(q)=r(i);
        uznew(q)=uz(i);
        uphinew(q)=uphi(i);
        q=q+1;
    end
end

num=trapz(rnew,uznew.*uphinew.*rnew.*rnew);
den=trapz(rnew,uznew.*uznew.*rnew);
S=num/den/Rref;