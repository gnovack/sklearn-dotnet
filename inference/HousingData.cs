using Microsoft.ML.OnnxRuntime.Tensors;

namespace aspnetcore
{
    public class HousingData
    {
        public float MedianIncome { get; set; }
        public float MedianHouseAge { get; set; }
        public float AverageNumberOfRooms { get; set; }
        public float AverageNumberOfBedrooms { get; set; }
        public float Population { get; set; }
        public float AverageOccupancy { get; set; }
        public float Latitude { get; set; }
        public float Longitude { get; set; }

        public Tensor<float> AsTensor() 
        {
            float[] data = new float[] 
            {
                MedianIncome, MedianHouseAge, AverageNumberOfRooms, AverageNumberOfBedrooms, 
                Population, AverageOccupancy, Latitude, Longitude 
            };
            int[] dimensions = new int[] { 1, 8 };
            return new DenseTensor<float>(data, dimensions);
        }
    }
}