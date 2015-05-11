function limpia = limpia(x)

xlimpio(1)=x(1);
q=1;
for i=1:length(x)
    if x(i)~=xlimpio(q)
        xlimpio(q+1)=x(i);
        q=q+1;
    end
end

limpia=xlimpio;