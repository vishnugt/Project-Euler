object Solution {
    
    def func(n : Long) : Long =  return n * (n + 1) / 2

    def main(args: Array[String]) {
        var t = Console.readInt();
        while(t > 0)
        {
            t = t - 1
            var n = Console.readLong() - 1
            println( func(n/3) * 3 + func(n/5) * 5 - func(n/15) * 15)
        }
    }
}