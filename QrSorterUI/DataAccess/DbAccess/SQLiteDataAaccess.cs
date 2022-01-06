using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.Extensions.Configuration;
using Microsoft.Data.Sqlite;
using Dapper;
using System.Data;

namespace DataAccess.DbAccess
{
    public class SQLiteDataAaccess : ISQLDataAaccess
    {
        private readonly IConfiguration _config;

        public SQLiteDataAaccess(IConfiguration config)
        {
            _config = config;
        }

        public async Task<IEnumerable<T>> LoadData<T>(string sql, string connectionId = "DefaultConnection")
        {
            using IDbConnection connection = new SqliteConnection(_config.GetConnectionString(connectionId));
            return await connection.QueryAsync<T>(sql);
        }

        public async Task<IEnumerable<T>> LoadData<T, U>(string sql, U data, string connectionId = "DefaultConnection")
        {
            using IDbConnection connection = new SqliteConnection(_config.GetConnectionString(connectionId));
            return await connection.QueryAsync<T>(sql, data);
        }

        public async Task SaveData<T>(string sql, T data, string connectionId = "DefaultConnection")
        {
            using IDbConnection connection = new SqliteConnection(_config.GetConnectionString(connectionId));
            await connection.ExecuteAsync(sql, data);
        }
    }
}
