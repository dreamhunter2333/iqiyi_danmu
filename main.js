res =[]
for (j = 1; j < 80; j++) {
    i = "".concat(60);
    n = t.tvid + "_" + i + "_" + j + "cbzuw1259a";
    r = "0000" + t.tvid;
    o = (0, Z.Z)(n).slice(-8);
    s = t.tvid + "_" + i + "_" + j + "_" + o + ".br";
    c = "https://cmts.iqiyi.com/bullet/" + r.substr(r.length - 4, 2) + "/" + r.substr(r.length - 2, 2) + "/" + s;
    res.push(c);
}
console.log(res)
