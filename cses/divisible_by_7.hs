import Data.Word (Word64)
import Text.Read (readMaybe)

main :: IO ()
main = do
  input <- getLine
  let maybeNumber = readMaybe input :: Maybe Word64
  let divisibleBy7 = case maybeNumber of
        Just num -> num `mod` 7 == 0
        Nothing -> False
  let divisibility = if divisibleBy7 then "divisible by 7" else "not divisible by 7"
  putStrLn $ "The number is " ++ divisibility ++ "."
