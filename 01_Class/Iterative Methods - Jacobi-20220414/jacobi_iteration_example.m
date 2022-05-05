A=[2 -1 0 0;-1 2 -1 0;0 -1 2 -1;0 0 -1 2]; b=[1;0;0;1];

m = length(A);
x=[0;0;0;0]; % starting point
tol=1e-8; 

n=0;
x0 = x;
xn = 1;
while xn > tol
    x(1) = (b(1)-( A(1,2)*x0(2) ) )/A(1,1);
    for i=2:m-1
        x(i) = (b(i)-( A(i,i-1)*x0(i-1) + A(i,i+1)*x0(i+1) ) )/A(i,i);
    end
    x(m) = (b(m)-(A(m,m-1)*x0(m-1)))/A(m,m);
    
    %xn = norm(x-x0,1);
    xn = norm(x-x0,2); 
    %xn = norm(x-x0,'inf');
    x0 = x;
    n = n+1;
end

disp('Jacobi')
disp('number of iterations =')
n
x