function makematrix=makematrix(u)

matrix = ones(58,59);
q=1;
for i=1:59
    for j=1:58
        matrix(j,i)=u(q);
        q=q+1;
    end
end

makematrix=matrix;
