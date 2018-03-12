function [X,Y] = F(x,y)
if x == 0 && (y <= -1 || y >= 1)
    error("Error! Input point belongs to the branch cut y^2 >= 1")
end
    
r = sqrt((1-x.^2-y.^2).^2+4*x.^2) / (x.^2 + (1+y).^2);

%Accounting for the fact that atan only returns theta on [-pi/2, pi/2] by
%adding/subtracting pi depending on quandrant to ensure that theta is
%defined on [-pi, pi).
if x >= 0
    theta = atan(2*x / (1 - x.^2 - y.^2));
end
if (x < 0 && (1 - x.^2 - y.^2) > 0)
    theta = atan(2*x / (1 - x.^2 - y.^2)) + pi;
end
if (x < 0 && (1 - x.^2 - y.^2) <= 0)
    theta = atan(2*x / (1 - x.^2 - y.^2)) - pi;
end

X = -sqrt(r) * cos(theta / 2);
Y = -sqrt(r) * sin(theta / 2);
end

