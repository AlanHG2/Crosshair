using Windows.UI.Xaml.Controls;
using System;
using Windows.UI.Xaml.Media.Imaging;

namespace Crosshair
{
    /// <summary>
    /// Página vacía que se puede usar de forma independiente o a la que se puede navegar dentro de un objeto Frame.
    /// </summary>
    public sealed partial class MainPage : Page
    {
        public MainPage()
        {
            this.InitializeComponent();
            LoadCrosshair();
        }

        private void LoadCrosshair()
        {
            // Crear un BitmapImage desde los recursos
            var crosshairImage = new BitmapImage(new Uri("ms-appx:///Assets/Crosshair7.png"));

            // Asignar la imagen al control Image en la UI
            CrosshairImage.Source = crosshairImage;
        }
    }
}
