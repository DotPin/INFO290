

import java.awt.Color;
import java.awt.image.BufferedImage;


public class WB extends Filtro {    
    private int r,g,b;
    private Color color;
    int umbral = 127;// 

    public WB(){}

   /*public BufferedImage set_Blanco_y_Negro(BufferedImage f){
        BufferedImage bn = new BufferedImage(f.getWidth(),f.getHeight(), BufferedImage.TYPE_BYTE_BINARY);
        //se traspasan los colores Pixel a Pixel
        for(int i=0;i<f.getWidth();i++)
          for(int j=0;j<f.getHeight();j++)
               bn.setRGB(i, j, f.getRGB(i, j));
        return bn;
   }*/

   public BufferedImage set_Blanco_y_Negro_con_Umbral(BufferedImage f){
        BufferedImage bn = new BufferedImage(f.getWidth(),f.getHeight(), BufferedImage.TYPE_BYTE_BINARY);        
        //se traspasan los colores Pixel a Pixel
        for(int i=0;i<f.getWidth();i++){
          for(int j=0;j<f.getHeight();j++){
               color = new Color(f.getRGB(i, j));
               //se extraen los valores RGB
                r = color.getRed();
                g = color.getGreen();
                b = color.getBlue();
                //dependiendo del valor del umbral, se van separando los
                // valores RGB a 0 y 255  
                r =(r>umbral)? 255: 0;
                g =(g>umbral)? 255: 0;
                b =(b>umbral)? 255: 0;
                bn.setRGB(i, j, new Color(r,g,b).getRGB());            
          }
        }        
        return bn;
    }
 
}
