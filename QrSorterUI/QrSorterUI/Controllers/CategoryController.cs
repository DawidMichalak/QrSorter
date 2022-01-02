using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using DataAccess.Models;
using DataAccess.Access;
using System.Threading.Tasks;
using System.Collections.Generic;
using AutoMapper;
using QrSorterUI.Models;

namespace QrSorterUI.Controllers
{
    public class CategoryController : Controller
    {
        private readonly IDataAccess<Category> _dataAccess;
        private readonly IMapper _mapper;

        public CategoryController(IDataAccess<Category> dataAccess, IMapper maper)
        {
            _dataAccess = dataAccess;
            _mapper = maper;
        }

        [HttpGet]
        public async Task<IActionResult> Index()
        {
            var categories = await GetCategories();
            return View(categories);
        }

        public async Task<IActionResult> GetPartialView()
        {
            var categories = await GetCategories();
            return PartialView("CategoryList", categories);
        }

        private async Task<List<CategoryViewModel>> GetCategories()
        {
            var entries = await _dataAccess.Get();
            var categories = new List<CategoryViewModel>();

            foreach (var dbEntity in entries)
            {
                categories.Add(_mapper.Map<CategoryViewModel>(dbEntity));
                var last = categories[categories.Count - 1].CategoryName.ToLower();
                categories[categories.Count - 1].CategoryName = last[0].ToString().ToUpper() + last.Substring(1);
            }

            return categories;
        }
    }
}
