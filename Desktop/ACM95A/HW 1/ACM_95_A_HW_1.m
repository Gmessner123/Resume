x = linspace(-2,1,1000);
y = linspace(-1.5,1.5,1000);
[X,Y] = meshgrid(x,y);
F = 0;
k = zeros(1000, 1000);
for n = 1:500
    F = F.^2 + X + 1i*Y;
    for i = 1:1000
        for j = 1:1000
            if abs(F(i,j)) > 2
                if k(i, j) == 0
                    k(i, j) = n;
                end
            end
        end
    end
end
for i = 1:1000
    for j = 1:1000
        if k(i,j) == 0
            k(i, j) = 501;
        end
    end
end

figure;
imagesc(x, y, k);
axis equal;
axis([-2, 1, -1.5, 1.5]);

x = linspace(-0.748766713922161, -0.748766707771757,1000);
y = linspace(0.123640844894862, 0.123640851045266,1000);
[X,Y] = meshgrid(x,y);
F = 0;
k = zeros(1000, 1000);
for n = 1:500
    F = F.^2 + X + 1i*Y;
    for i = 1:1000
        for j = 1:1000
            if abs(F(i,j)) > 2
                if k(i, j) == 0
                    k(i, j) = n;
                end
            end
        end
    end
end
for i = 1:1000
    for j = 1:1000
        if k(i,j) == 0
            k(i, j) = 501;
        end
    end
end

figure;
imagesc(x, y, k);
axis equal;
axis([-0.748766713922161, -0.748766707771757, 0.123640844894862, 0.123640851045266]);