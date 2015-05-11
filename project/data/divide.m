function xnew=divide(x,n)

q=1;
for i=1:length(x)-1
    xnew(q:(q+n))=linspace(x(i),x(i+1),n+1);
    q=q+n*i;
end
