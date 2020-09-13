subroutine sobel(n, m, im, imx, imy, imxy)
  implicit none
  integer, intent(in) :: n,m
  integer(kind=4), dimension(:,:), intent(in) :: im 
  integer(kind=4), dimension(:,:), intent(inout) :: imx, imy, imxy

  integer :: i,j
  integer(kind=4) :: valuex, valuey

  do i=2,n-1
    do j=2,m-1

      valuex = 2*im(i,j-1) + im(i-1,j-1) + im(i+1,j-1) 
      valuex = valuex -2*im(i,j+1) - im(i-1,j+1) -im(i+1,j+1)
      imx(i,j) = abs(valuex)

      valuey = 2*im(i-1,j) + im(i-1,j+1) + im(i-1,j-1)
      valuey = valuey - 2*im(i+1,j) -  im(i+1,j+1) - im(i+1,j-1)
      imy(i,j) = abs(valuey)

      imxy(i,j) = sqrt(1.*valuex**2+1.*valuey**2)/sqrt(2.)
    end do
  end do
end subroutine sobel
