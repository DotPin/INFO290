

import java.awt.color.ColorSpace;
import java.awt.image.BufferedImage;
import java.awt.image.ColorConvertOp;
/**
 * @web http://jc-mouse.blogspot.com/
 * @author Mouse
 */
public class Grises {
    private BufferedImage foto=null;

    public Grises(){}

     public void set_Escala_de_Grises(BufferedImage f){
       ColorConvertOp ccop = new ColorConvertOp(ColorSpace.getInstance(ColorSpace.CS_GRAY), null);
       foto = ccop.filter((BufferedImage)f,null);
    }

    public BufferedImage getFotoGris(){
        return this.foto;
    }

}
