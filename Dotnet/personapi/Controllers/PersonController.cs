using Microsoft.AspNetCore.Mvc;

namespace personapi.Controllers
{
    [ApiController]
    [Route("api/persons")]
    public class PersonController : ControllerBase
    {
        [HttpGet]
        [Route("")]
        public List<IPerson> Persons()
        {

            string filePath = "./data.txt";
            List<IPerson> persons = new List<IPerson>();
            string[] lines = System.IO.File.ReadAllLines(filePath);
            foreach (var line in lines)
            {
                string[] values = line.Split(',');
                if (values.Length == 3)
                {
                    persons.Add(new Person
                    {
                        Name = values[0],
                        Address = values[1],
                        Country = values[2]
                    });
                }
            }

            persons = persons.OrderBy(p => p.Name).ToList();
            return persons;
        }
    }

    internal class Person : IPerson
    {
        public string Name { get; set; }
        public string Address { get; set; }
        public string Country { get; set; }
    }

    public interface IPerson
    {
        string Name { get; set; }
        string Address { get; set; }
        string Country { get; set; }
    }
}
