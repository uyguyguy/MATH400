function x = part_piv_ge_1 ( A, b )

%GAUSS_ELIM   solve the linear system Ax = b using Gaussian elimination
%             with back substitution
%             This version has partial pivoting
%     calling sequences:
%             x = part_piv_ge_1 ( A, b )
%             part_piv_ge_1 ( A, b )
%
%     inputs:
%             A       coefficient matrix for linear system
%                     (matrix must be square)
%             b       right-hand side vector
%
%     output:
%             x       solution vector (i.e., vector for which Ax = b)
%

%

[nrow,ncol] = size ( A );
if ( nrow ~= ncol )
   disp ( 'gauss_elim error: Square coefficient matrix required' );
   return;
end
nb = length ( b );
if ( nrow ~= nb )
   disp ( 'gauss_elim error: Size of b-vector not compatible with matrix dimension' )
   return;
end

x = zeros ( 1, nrow );

%
%    Gaussian elimination
%
for i = 1 : nrow - 1
    [x,t]=max(abs(A(i:nrow,i))); t=t+i-1;
    temp=A(i,:);        tb=b(i);
    A(i,:) = A(t,:);    b(i)=b(t);
    A(t,:) = temp;      b(t)=tb;
    aii=A(i,i);
    for j = i+1 : nrow
	    m = -A(j,i) / aii; % multiplier
		A(j,i) = 0;
		A(j, i+1:nrow) = A(j, i+1:nrow) + m * A(i, i+1:nrow);
		b(j) = b(j) + m * b(i);
    end
    [A b]
    pause
end

%
%    back substitution
%

x(nrow) = b(nrow) / A(nrow, nrow);
for i = nrow - 1 : -1 : 1
    x(i) = ( b(i) - sum ( x(i+1:nrow) .* A(i, i+1:nrow) ) ) / A(i,i);
end
