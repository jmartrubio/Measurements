function center = calculatedCenter(caso,method)

switch caso
    case 'SR03'
        switch method
            case '1'
                center = [ -0.675757291337286   0.700673039840059];
            case '2'
                center = [  -1.198795553691046  -0.050637582815586];
        end
        
    case 'SR04'
        switch method
            case '1'
                center = [-4.067164794473344  -0.637458344590814];
            case '2'
                center = [ -4.260711602493318  -0.472646453795124];
        end
        
    case 'SR05'        
        switch method
            case '1'
                center = [ -7.291627677439617  -0.513641010007193];
            case '2'
                center = [ -6.175431318905359  -0.073142591053518];
        end
        
end
    