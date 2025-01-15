package com.regnosys.rosetta.generator.python.util;

import java.util.HashSet;
import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.Set;
import java.util.function.Function;
import com.regnosys.rosetta.rosetta.RosettaType;
import com.regnosys.rosetta.rosetta.RosettaModel;

public class Util {

    public static <T> Iterable<T> distinct(Iterable<T> parentIterable) {
        return new DistinctByIterator<>(parentIterable, Function.identity());
    }

    public static <T, U> Iterable<T> distinctBy(Iterable<T> parentIterable, Function<T, U> extractFunction) {
        return new DistinctByIterator<>(parentIterable, extractFunction);
    }

    public static <T> boolean exists(Iterable<?> iter, Class<T> clazz) {
        for (Object item : iter) {
            if (clazz.isInstance(item)) {
                return true;
            }
        }
        return false;
    }

    public static String getNamespace(RosettaModel rm) {
        return rm.getName().split("\\.")[0];
    }

    private static class DistinctByIterator<T, U> implements Iterable<T> {
        private final Iterable<T> iterable;
        private final Function<T, U> extractFunction;

        public DistinctByIterator(Iterable<T> iterable, Function<T, U> extractFunction) {
            this.iterable = iterable;
            this.extractFunction = extractFunction;
        }

        @Override
        public Iterator<T> iterator() {
            return new Iterator<T>() {
                private final Iterator<T> parentIterator = iterable.iterator();
                private final Set<U> read = new HashSet<>();
                private T readNext = null;

                @Override
                public boolean hasNext() {
                    while (readNext == null && parentIterator.hasNext()) {
                        T next = parentIterator.next();
                        U compareVal = extractFunction.apply(next);
                        if (read.add(compareVal)) {
                            readNext = next;
                        }
                    }
                    return readNext != null;
                }

                @Override
                public T next() {
                    if (!hasNext()) {
                        throw new NoSuchElementException("read past end of iterator");
                    }
                    T result = readNext;
                    readNext = null;
                    return result;
                }
            };
        }
    }

    public static String fullname(RosettaType clazz) {
        return clazz.getModel().getName() + "." + clazz.getName();
    }

    public static String packageName(RosettaType clazz) {
        return clazz.getModel().getName();
    }
}