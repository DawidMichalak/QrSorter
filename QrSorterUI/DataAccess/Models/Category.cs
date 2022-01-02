using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DataAccess.Models
{
    public class Category
    {
        public int Id { get; set; }
        public string CategoryName { get; set; }
        public int NumberOfProducts { get; set; }
        public int BoxId { get; set; }
    }
}
