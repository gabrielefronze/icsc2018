// Interfaces
import java.util.Collection;

// Data structures
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.HashSet;
import java.util.TreeSet;

// Utility
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Collections;

public class JavaCollectionsTest
{

    public static void main(String[] args)
    {
        // TODO pass runTest an empty collection to test it
        runTest(...);
    }

    public static void runTest(final Collection<String> strings)
    {
        time(() -> readStrings("../data/random_strings.txt", strings), "File read");
        time(() -> testIterate(strings), "Iterate  ");
        time(() -> testContains(strings), "Contains ");
        time(() -> testRemove(strings), "Remove   ");
    }

    public static void testIterate(final Collection<String> collection)
    {
        for (final String s : collection)
        {
        }
    }

    public static void testContains(final Collection<String> collection)
    {
        for (final String s : collection)
        {
            collection.contains(s);
        }
    }

    public static void testRemove(final Collection<String> collection)
    {
        for (final String s : new LinkedList<String>(collection))
        {
            collection.remove(s);
        }
    }

    public static void time(final Runnable r, final String label)
    {
        final long startTime = System.nanoTime();
        r.run();
        final long endTime = System.nanoTime();
        final double duration = (endTime - startTime) / 1000000.;
        System.out.println(label + " ran in " + duration + " ms");
    }

    public static void readStrings(final String fileName, final Collection<String> collection)
    {
        try (final BufferedReader reader = new BufferedReader(new FileReader(fileName)))
        {
            String line;
            while ((line = reader.readLine()) != null)
            {
                collection.add(line);
            }
        }
        catch (final java.io.FileNotFoundException ex)
        {
            System.err.println("Unable to open file: " + fileName);
        }
        catch (final java.io.IOException ex)
        {
            System.err.println("Error reading file: " + fileName);                  
        }
    }
}

