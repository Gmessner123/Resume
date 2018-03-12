addpath('randomDisk.m');
z=randomDisk(0,1,10000);
f = (1 + z).^i;
g = 1 + 1i*z + .5i.*(1i-1)*z.^2;
diff = abs(f - g);
x = real(z);
y = imag(z);
scatter(x,y,[],diff,'filled')
colorbar
