function [x,y]=reduceVector(ax,ay,min,max)

q=1;
for i=1:length(ax)
    if (ax(i)>min) && (ax(i)<max) && (ay(i)<max) && (ay(i)>min)
        x(q)=ax(i);
        y(q)=ay(i);
        q=q+1;
    end
end
