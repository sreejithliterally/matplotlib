import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257]
y1 = [1.9397, 1.8089, 1.7074, 1.6207, 1.5608, 1.513, 1.4703, 1.44, 1.4079, 1.3713, 1.3351, 1.3216, 1.2836, 1.2762, 1.2616, 1.2412, 1.2083, 1.195, 1.1946, 1.1621, 1.146, 1.1256, 1.1197, 1.1048, 1.0881, 1.0907, 1.0907, 1.064, 1.0718, 1.0511, 1.024, 1.0288, 1.0334, 1.025, 1.0194, 1.0018, 1.0089, 1.0061, 1.0092, 0.9833, 0.9702, 0.966, 0.9642, 0.9803, 0.9642, 0.9617, 0.9573, 0.9453, 0.9637, 0.9497, 0.9387, 0.9416, 0.9637, 0.9312, 0.9242, 0.9155, 0.9316, 0.9229, 0.9449, 0.9109, 0.921, 0.9257, 0.9086, 0.9208, 0.8875, 0.9021, 0.9187, 0.9, 0.877, 0.9052, 0.9015, 0.8852, 0.9081, 0.907, 0.8832, 0.8616, 0.8907, 0.8931, 0.8994, 0.8678, 0.866, 0.8709, 0.8761, 0.8688, 0.8771, 0.8593, 0.8794, 0.863, 0.8635, 0.8673, 0.8589, 0.8556, 0.8472, 0.8552, 0.8634, 0.8674, 0.8417, 0.8526, 0.8461, 0.8386, 0.8515, 0.8638, 0.8627, 0.8505, 0.8417, 0.8271, 0.8573, 0.8533, 0.8188, 0.8395, 0.8405, 0.8273, 0.8415, 0.8423, 0.8235, 0.796, 0.847, 0.8371, 0.8254, 0.8438, 0.8287, 0.8165, 0.82, 0.8204, 0.8426, 0.8203, 0.7999, 0.8216, 0.825, 0.8368, 0.8177, 0.8136, 0.8078, 0.8055, 0.8146, 0.8079, 0.8101, 0.8329, 0.8336, 0.818, 0.8216, 0.8159, 0.8272, 0.8119, 0.8112, 0.8042, 0.8258, 0.8193, 0.8035, 0.8225, 0.808, 0.8018, 0.8215, 0.8271, 0.821, 0.8152, 0.7956, 0.8153, 0.8193, 0.7891, 0.7975, 0.7972, 0.8041, 0.7975, 0.8065, 0.8157, 0.8142, 0.7957, 0.7972, 0.8155, 0.8083, 0.7778, 0.8082, 0.8086, 0.8042, 0.8149, 0.7872, 0.7952, 0.8086, 0.8013, 0.8112, 0.7986, 0.8049, 0.7927, 0.8182, 0.7999, 0.8027, 0.7997, 0.8088, 0.8079, 0.7766, 0.7731, 0.786, 0.7823, 0.7714, 0.777, 0.8115, 0.7928, 0.8054, 0.7822, 0.8034, 0.7907, 0.791, 0.7763, 0.7843, 0.7958, 0.7716, 0.7863, 0.7903, 0.7733, 0.8078, 0.8004, 0.794, 0.7744, 0.7779, 0.7852, 0.8069, 0.8172, 0.7885, 0.7959, 0.7842, 0.7753, 0.784, 0.7884, 0.7612, 0.7829, 0.7704, 0.7852, 0.7877, 0.7818, 0.7987, 0.7881, 0.7903, 0.7971, 0.7789, 0.795, 0.7957, 0.7895, 0.7734, 0.7798, 0.7756, 0.7852, 0.7727, 0.7832, 0.7854, 0.7722, 0.7895, 0.7761, 0.7757, 0.7914, 0.7776, 0.7568, 0.7867, 0.7811, 0.7775, 0.7969, 0.7567]
y2 = [1.8449, 1.7143, 1.5916, 1.4983, 1.4222, 1.3579, 1.3046, 1.2566, 1.2155, 1.1743, 1.1336, 1.1019, 1.0675, 1.0342, 1.0082, 0.9815, 0.955, 0.9276, 0.9112, 0.8922, 0.8686, 0.8568, 0.8339, 0.8248, 0.8023, 0.789, 0.7788, 0.7666, 0.7574, 0.7456, 0.7356, 0.7247, 0.7207, 0.7105, 0.7008, 0.6962, 0.6889, 0.6841, 0.6758, 0.6643, 0.6551, 0.6499, 0.6459, 0.6452, 0.6333, 0.6345, 0.6233, 0.621, 0.6215, 0.616, 0.6068, 0.6102, 0.6105, 0.6052, 0.594, 0.5911, 0.591, 0.5841, 0.5842, 0.5875, 0.5879, 0.5812, 0.5806, 0.5741, 0.5706, 0.5668, 0.5681, 0.5647, 0.5601, 0.5624, 0.5651, 0.5519, 0.563, 0.5597, 0.5519, 0.5499, 0.5461, 0.5482, 0.5532, 0.5415, 0.5384, 0.5366, 0.5404, 0.5338, 0.5383, 0.5371, 0.5311, 0.5277, 0.5317, 0.5347, 0.53, 0.5301, 0.5254, 0.5229, 0.5252, 0.523, 0.5151, 0.5199, 0.5248, 0.5102, 0.511, 0.5223, 0.5128, 0.5112, 0.5113, 0.5046, 0.5062, 0.5162, 0.5074, 0.497, 0.4976, 0.5052, 0.5065, 0.5063, 0.4992, 0.4905, 0.4924, 0.4971, 0.4923, 0.504, 0.5013, 0.5037, 0.4967, 0.504, 0.4946, 0.4979, 0.4947, 0.4939, 0.4894, 0.4928, 0.4958, 0.4816, 0.4919, 0.4871, 0.4875, 0.483, 0.4776, 0.4817, 0.4947, 0.4808, 0.4845, 0.4809, 0.4827, 0.4839, 0.4767, 0.4799, 0.4811, 0.4844, 0.4903, 0.4834, 0.4803, 0.4717, 0.4778, 0.4848, 0.4847, 0.4771, 0.4731, 0.4775, 0.4832, 0.4807, 0.4777, 0.4807, 0.4762, 0.4711, 0.4731, 0.4826, 0.4718, 0.4714, 0.4837, 0.4718, 0.483, 0.4728, 0.4735, 0.4664, 0.4668, 0.4706, 0.4717, 0.4658, 0.4629, 0.4728, 0.4716, 0.4647, 0.4699, 0.4655, 0.472, 0.4746, 0.4691, 0.4753, 0.4701, 0.4746, 0.4576, 0.4606, 0.4581, 0.4631, 0.4602, 0.4561, 0.4544, 0.4574, 0.466, 0.4575, 0.4592, 0.4651, 0.4551, 0.4562, 0.4635, 0.4595, 0.4589, 0.4515, 0.4583, 0.452, 0.4608, 0.4674, 0.46, 0.4575, 0.4634, 0.4566, 0.458, 0.4601, 0.458, 0.4559, 0.4556, 0.4548, 0.45, 0.4581, 0.4466, 0.446, 0.4537, 0.4586, 0.4502, 0.4501, 0.4422, 0.4509, 0.4593, 0.4538, 0.4511, 0.4554, 0.4382, 0.4432, 0.4486, 0.4417, 0.4407, 0.4473, 0.4392, 0.4469, 0.4458, 0.4449, 0.445, 0.449, 0.4468, 0.4543, 0.4424, 0.4491, 0.4487, 0.447, 0.4466, 0.4422, 0.4409]



plt.plot(x, y1, label ='train loss')
plt.plot(x, y2, label ='val loss')



plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.title('Model Loss')
plt.show()