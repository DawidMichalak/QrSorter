using System.Collections.Generic;
using System.Threading.Tasks;

namespace DataAccess.Access
{
    public interface IDataAccess<T>
    {
        Task Delete(int id);
        Task<IEnumerable<T>> Get();
        Task<T> Get(int id);
        Task Insert(T entity);
        Task Update(T entity);
    }
}
