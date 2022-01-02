using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using DataAccess.Models;
using DataAccess.DbAccess;
using Dapper;

namespace DataAccess.Access
{
    public class CategoryAccess : IDataAccess<Category>
    {
        private readonly ISQLDataAaccess _db;

        public CategoryAccess(ISQLDataAaccess db)
        {
            _db = db;
        }

        public Task<IEnumerable<Category>> Get()
        {
            string sql = "select * from Categories";
            return _db.LoadData<Category>(sql);
        }

        public async Task<Category> Get(int categoryId)
        {
            string sql = "select * from Categories where id = :Id";

            DynamicParameters dynamicParameters = new DynamicParameters(new
            {
                Id = categoryId
            });

            var results = await _db.LoadData<Category, DynamicParameters>(sql, dynamicParameters);
            return results.First();
        }

        public Task Insert(Category category)
        {
            string sql = "insert into Categories(categoryName, numberOfProducts, boxId) values(:CategoryName, :NumberOfProducts, BoxId)";

            DynamicParameters dynamicParameters = new DynamicParameters(new
            {
                CategoryName = category.CategoryName,
                NumberOfProducts = category.NumberOfProducts,
                BoxId = category.BoxId
            });

            return _db.SaveData(sql, dynamicParameters);
        }

        public Task Update(Category category)
        {
            string sql = @"update Categories 
                           set categoryName = :CategoryName, 
                           set numberOfProducts, 
                           set boxId = :BoxId
                           where id = :Id";

            DynamicParameters dynamicParameters = new DynamicParameters(new
            {
                Id = category.Id,
                CategoryName = category.CategoryName,
                NumberOfProducts = category.NumberOfProducts,
                BoxId = category.BoxId
            });

            return _db.SaveData(sql, dynamicParameters);
        }

        public Task Delete(int categoryId)
        {
            string sql = "delete from Categories where id = :Id";

            DynamicParameters dynamicParameters = new DynamicParameters(new
            {
                Id = categoryId
            });

            return _db.SaveData(sql, dynamicParameters);
        }
    }
}
