package bubblesort

func BubbleSort(values []int) {
	changed := false

	for i := 0; i < len(values)-1; i++ {
		changed = false
		for j := 0; j < len(values)-1-i; j++ {
			if values[j] > values[j+1] {
				values[j], values[j+1] = values[j+1], values[j]
				changed = true
			}
		}
		if changed == false {
			break
		}
	}
}
