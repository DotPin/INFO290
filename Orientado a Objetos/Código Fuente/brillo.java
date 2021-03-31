

import java.awt.Canvas;
import java.awt.image.*;
import java.awt.Image;
import javax.swing.*;
import java.awt.Graphics;
import java.awt.image.BufferedImage;


public class brillo extends Canvas {
    
    BufferedImage bufferedImageDeSalida;
    Image imagenModificada = null;
   
    public BufferedImage activar(BufferedImage intensidad,int ingreso){
        System.out.println("numero de ingreso desde clase brillo = "+ingreso);
        
        int p, rojo, verde, azul;
        int a = intensidad.getWidth(); //Ancho
        int h = intensidad.getHeight(); //Alto
        int totalDePixeles = a * h;
        int pixeles[] = new int[totalDePixeles]; //Arreglo de pixeles
        PixelGrabber pg = new PixelGrabber(intensidad,0,0,a,h,pixeles,0,a);
        try
        {
            pg.grabPixels();
            for(int i = 0; i < totalDePixeles; i++){
                p = pixeles[i]; //Valor de un pixel
                rojo = (0xff & (p>>16)) + ingreso; //Desplaza el entero p 16 bits a la derecha yaplica la operacion AND a los primeros 8 bits
                verde = (0xff & (p>>8)) + ingreso; //Desplaza el entero p 8 bits a la derecha yaplica la operacion AND a los siguientes 8 bits
                azul = (0xff & p) + ingreso; //Aplica la operacion AND a los siguientes 8bits
                if(rojo>255) rojo=255;
                if(verde>255) verde=255;
                if(azul>255) azul=255;
                if(rojo<0) rojo=0;
                if(verde<0) verde=0;
                if(azul<0) azul=0;
                pixeles[i]=(0xff000000|rojo<<16|verde<<8|azul);
            }
            imagenModificada = createImage(new MemoryImageSource(a,h,pixeles,0,a));
            bufferedImageDeSalida = new BufferedImage(imagenModificada.getWidth(this), imagenModificada.getHeight(this), BufferedImage.TYPE_INT_RGB);
            Graphics g = bufferedImageDeSalida.getGraphics();
            g.drawImage(imagenModificada, 0, 0, null);
            
        }catch(InterruptedException e){
            JOptionPane.showMessageDialog(null,e.getMessage(),"Respuesta",JOptionPane.ERROR_MESSAGE);
        }
    return bufferedImageDeSalida;
    }
}