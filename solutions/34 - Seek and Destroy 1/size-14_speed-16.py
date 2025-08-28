-- 7 Billion Humans (2235) --
-- 34: Seek and Destroy 1 --

mem4 = nearest shredder
mem1 = nearest datacube
step mem1
a:
mem2 = set c
b:
step n
mem1 = nearest datacube
if n == wall:
	pickup mem2
	giveto mem4
	end
endif
if mem1 >= mem2:
	jump b
else:
	jump a
endif

