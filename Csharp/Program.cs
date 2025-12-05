 

// Methode pour les list contenant uniquement des Integers


List<int> arr1 = new List<int> { 1, 2, 3 };
List<int> arr2 = new List<int> { 3, 4, 5 };

List<int> arrContains=new List<int>(); 
List<int> difference(List<int> arr1, List<int> arr2)
{
    foreach(int i in arr1)
    {
        if (!arr2.Contains(i))
            arrContains.Add(i);
        
    }

    foreach(int i in arr2)
    {
        if (!arr1.Contains(i))
            arrContains.Add(i);
        
    }

    foreach (int i in arrContains)
    {
        Console.Write(i+",");
    }

    return arrContains;
}

Console.WriteLine("1er test : ");
difference(arr1, arr2);
//arrContains.Clear();
Console.WriteLine("");

 
// Methode pour les list contenant uniquement des String

List<string> arr1Str = new List<string> { "a", "b" };
List<string> arr2Str = new List<string> { "b","c" };

List<string> arrContainsStr=new List<string>(); 

List<string> differenceStr(List<string> arr1, List<string> arr2)
{
    foreach(string i in arr1)
    {
        if (!arr2.Contains(i))
            arrContainsStr.Add(i);
        
    }

    foreach(string i in arr2)
    {
        if (!arr1.Contains(i))
            arrContainsStr.Add(i);
        
    }

    foreach (string i in arrContainsStr)
    {
        Console.Write(i+",");
    }

    return arrContainsStr;
}


Console.WriteLine("1er test String : ");

differenceStr(arr1Str,arr2Str);

