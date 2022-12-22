import * as nested from "@pulumi/nested";
import * as random from "@pulumi/random";

const output = new random.RandomString("random", {
    length: 12,
});

const ok = new nested.NoDefault("nothing", {
    value: "cat",
    nested: {
        value: output.result,
    },
});

// Comment out the below to get a successful preview/update.
const result = new nested.HasDefault("nothing", {
    value: "cat",
    nested: {
        value: output.result,
    },
});
