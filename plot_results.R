library(tidyverse)
library(readr)

chat_mo_results <- read_csv("chat_mo_results.csv")

d2p = chat_mo_results %>% group_by(model, prompt_type) %>% 
  summarise(count = sum(agree)) %>% ungroup() %>%
  group_by(model) %>% summarise(result = max(count))%>% 
  add_row(model = 'llama-v2-30b-chat-ggml', result = 14) %>%
  arrange((result)) %>%
  mutate(Accuracy = result / 15) %>%
  select(model, Accuracy)

d2p$model = factor(d2p$model, levels = d2p$model )

ggplot(d2p, aes(model, Accuracy, fill = as.factor(model), color = as.factor(model))) +
  geom_col()+
  scale_fill_brewer(palette = 'Dark2')+
  scale_color_brewer(palette = 'Dark2')+
  theme_bw()+
  coord_flip()+
  theme(legend.position = 'none', text = element_text(size = 18))+
  scale_y_continuous(labels = scales::percent)+
  theme(panel.background = element_rect(fill = "grey15"),
        panel.grid.major = element_line(color = "grey45"),
        panel.grid.minor = element_line(color = "grey25"))+
  xlab('')+
  ylab('MO Classification Accuracy')+
  scale_x_discrete(labels=c('Orca-mini','MPT','Nous Hermes','Llama 2','ChatGPT', 'GPT-4'))



df <- data.frame(trt = c("a", "b", "c"), outcome = c(2.3, 1.9, 3.2))
ggplot(df, aes(trt, outcome)) +
  geom_col()