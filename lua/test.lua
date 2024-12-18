-- This is a comment

-- example for-loop
for i = 5, 10 do
  print(i)
end

-- conditionals

local fuck = "quarter"
local non_fuck = "squarter"

if fuck == non_fuck then
  print("yes")
elseif fuck ~= non_fuck then
  print(io.read()) -- io.read() is the input() equivalent
end

Num = 2

repeat
  print("gawgmeister")
  Num = Num - 1
until Num == 0
--if you write a bigger number than the original value, the 
--value doesn't go to that number if you're decreasing the value, 
--making an infinite loop.

Num = nil -- deletes

-- functions

function sin(x)
  print(math.sin(x))
end

print(sin(math.pi))

-- adder functions or functions inside functions

function lol(x)
  return function (y) return x*y end -- this function is used when lol() is called
end

-- allocate = lol(9)
-- print(allocate(5))
print(lol(16)(8)) -- instead of using another variable, add the param like this

-- tables

myTable = {
  conc = "non", -- use variable-like allocation for keys
  cunt = "cat"
}

print(myTable.conc)

myTable_but_better = {
  ["fucker"] = "unfuck the world, bitch", -- use this for non-var like keys
  [55] = 66
}

for key, val in pairs(myTable_but_better) do -- iterating on tables
  print(key, val)
end

Table_but_list = {1, 23, "sexmonster"}

for i = 1, #Table_but_list do print(i) end

-- metatables and metamethods
--
-- i don't really get it



