using AutoMapper;
using DataAccess.Models;
using QrSorterUI.Models;

namespace VetClinic.Mappings
{
    public class MappingProfile : Profile
    {
        public MappingProfile()
        {
            CreateMap<Category, CategoryViewModel>().ReverseMap();
        }
    }
}
