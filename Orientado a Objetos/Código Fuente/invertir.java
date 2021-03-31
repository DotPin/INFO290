
import java.awt.Color;
import java.awt.image.BufferedImage;


public class invertir extends Filtro {
    private BufferedImage foto;
    private int r,g,b;
    private Color color;
    public invertir(){}
     
 /* Invierte los bytes de una imagen */
	public void SetInvertir(BufferedImage f){
        this.foto = f;
        for(int i=0;i<foto.getWidth();i++){
          for(int j=0;j<foto.getHeight();j++){
                //se obtiene el color del pixel
                color = new Color(foto.getRGB(i, j));
                //se extraen los valores RGB
                r = color.getRed();
                g = color.getGreen();
                b = color.getBlue();
                //se coloca en la nueva imagen con los valores invertidos
                foto.setRGB(i, j, new Color(255-r,255-g,255-b).getRGB());                                                                    
          }
        }        
    }
    
    public BufferedImage getFoto(){
        return this.foto;
    }
}
