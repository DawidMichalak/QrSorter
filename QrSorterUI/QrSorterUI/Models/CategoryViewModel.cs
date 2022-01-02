using System.ComponentModel.DataAnnotations;
using System.ComponentModel;

namespace QrSorterUI.Models
{
    public class CategoryViewModel
    {
        public int Id { get; set; }

        [DisplayName("Category name")]
        public string CategoryName { get; set; }

        [DisplayName("Products")]
        public int NumberOfProducts { get; set; }

        [DisplayName("Box")]
        public int BoxId { get; set; }
    }
}
